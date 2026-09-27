"""Accounting checks for asset amortisation and exchange difference vouchers."""
import tempfile
import unittest
from pathlib import Path

import fixed_assets
from database import Database


class AssetAndDoeTest(unittest.TestCase):
    def setUp(self):
        self.folder=tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.db=Database(Path(self.folder.name)/"company.db")
        self.db.initialize("secret12345")

    def test_monthly_amortisation_posts_balanced_and_once(self):
        asset=fixed_assets.save_asset(self.db,{"asset_code":"LAP-1","name":"Laptop","acquired_on":"01-01-2024",
            "start_on":"01-01-2024","currency":"USD","cost":"1200","residual":"120","useful_months":12,
            "frequency":"monthly","asset_account":"211","depreciation_account":"6811","accumulated_account":"2811"})
        periods=fixed_assets.schedule(self.db,asset["id"])
        self.assertEqual(len(periods),12)
        self.assertEqual(sum(float(row["amount"]) for row in periods),1080)
        result=fixed_assets.post_period(self.db,asset["id"],periods[0]["period_end"],1)
        details=self.db.journal_voucher_detail(result["voucher"]["id"])
        self.assertEqual([(row["account_code"],row["debit"],row["credit"]) for row in details["lines"]],
                         [("6811",90.0,0.0),("2811",0.0,90.0)])
        with self.assertRaisesRegex(ValueError,"already posted"):
            fixed_assets.post_period(self.db,asset["id"],periods[0]["period_end"],1)
        with self.assertRaisesRegex(ValueError,"cannot be deleted"):
            fixed_assets.delete_asset(self.db,asset["id"])

    def test_yearly_amortisation_sums_partial_years(self):
        asset=fixed_assets.save_asset(self.db,{"asset_code":"EQ-1","name":"Equipment","acquired_on":"01-03-2024",
            "start_on":"01-03-2024","currency":"USD","cost":"1200","residual":"0","useful_months":12,
            "frequency":"yearly","asset_account":"211","depreciation_account":"6811","accumulated_account":"2811"})
        self.assertEqual([(row["period_end"],row["amount"]) for row in fixed_assets.schedule(self.db,asset["id"])],
                         [("2024-12-31","1000.00"),("2025-02-28","200.00")])

    def test_doe_enforces_class_and_gain_loss_sides(self):
        with self.assertRaisesRegex(ValueError,"gains credit"):
            self.db.save_journal_voucher({"entry_date":"01-09-2024","description":"DOE","currency":"LBP","voucher_type":"07"},
                [{"account_code":"4011","credit":"100"},{"account_code":"775100000","debit":"100"}],1)
        saved=self.db.save_journal_voucher({"entry_date":"01-09-2024","description":"DOE","currency":"LBP","voucher_type":"07"},
            [{"account_code":"4011","credit":"100"},{"account_code":"675100000","debit":"100"}],1)
        self.assertEqual(saved["voucher"]["voucher_type"],"07")
        self.assertEqual(saved["voucher"]["entry_date"],"01-09-2024")


if __name__=="__main__": unittest.main()
