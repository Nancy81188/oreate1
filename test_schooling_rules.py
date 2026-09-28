"""Schooling grant rates are date-effective and editable apart from tax exemption."""
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from database import Database


class SchoolingRulesTest(unittest.TestCase):
    def test_decrees_and_manual_period_override(self):
        with TemporaryDirectory() as folder:
            db=Database(Path(folder)/"company.db")
            db.initialize("secret12345")
            with db.connect() as connection:
                user=connection.execute("SELECT id FROM users WHERE username='admin'").fetchone()[0]
            db.apply_lebanese_payroll_rules(user)
            april=db.payroll_settings_for("2024-04-30")
            may=db.payroll_settings_for("2026-05-31")
            july=db.payroll_settings_for("2026-07-31")
            self.assertEqual((april["schooling_public_child"],april["schooling_private_child"]),("4000000","12000000"))
            self.assertEqual((may["schooling_public_cap"],may["schooling_private_cap"]),("12000000","36000000"))
            self.assertEqual((july["schooling_public_child"],july["schooling_private_child"]),("12000000","36000000"))
            self.assertEqual((july["schooling_public_cap"],july["schooling_private_cap"]),("36000000","108000000"))
            self.assertEqual(july["schooling_annual_exempt"],may["schooling_annual_exempt"])
            db.save_payroll_settings({**july,"schooling_private_child":"37000000"},user)
            self.assertEqual(db.payroll_settings_for("2026-07-31")["schooling_private_child"],"37000000")
            self.assertEqual(db.payroll_settings_for("2026-05-31")["schooling_private_child"],"12000000")


if __name__=="__main__":
    unittest.main()
