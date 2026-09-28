"""Dashboard totals keep their meaning while SQLite aggregates the source rows."""
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from database import Database


class DashboardAggregationTest(unittest.TestCase):
    def test_multiple_currencies_expenses_and_overdue_exclude_cancelled(self):
        with TemporaryDirectory() as folder:
            data = Database(Path(folder) / "dashboard.db")
            with data.connect() as db:
                db.executescript("""
                    CREATE TABLE invoices (
                        kind TEXT, currency TEXT, subtotal TEXT, total TEXT,
                        amount_paid TEXT, due_date TEXT, status TEXT, invoice_date TEXT
                    );
                    CREATE TABLE expenses (currency TEXT, subtotal TEXT);
                """)
                db.executemany("INSERT INTO invoices VALUES(?,?,?,?,?,?,?,?)", [
                    ("sale","USD","100","111","20","01-01-2000","posted","15-01-2026"),
                    ("sale","USD","50","55","55","01-01-2000","posted","20-01-2026"),
                    ("purchase","USD","40","44","4",None,"posted","20-01-2026"),
                    ("sale","EUR","25","27.75","0",None,"posted","20-02-2026"),
                    ("sale","USD","999","999","0","01-01-2000","cancelled","20-02-2026"),
                ])
                db.executemany("INSERT INTO expenses VALUES(?,?)", [("USD","5"),("USD","8")])
            # A dashboard read should not pull every expense row through list_expenses.
            data.list_expenses = lambda: self.fail("full expense rows were loaded")
            result = data.professional_dashboard()
            by_currency = {row["currency"]: row for row in result["metrics"]}
            self.assertEqual(by_currency["USD"], {
                "currency":"USD","sales":150.0,"purchases":40.0,"expenses":13.0,
                "profit":97.0,"receivables":91.0,"payables":40.0,"overdue":1
            })
            self.assertEqual(by_currency["EUR"]["sales"],25.0)
            self.assertEqual(by_currency["EUR"]["overdue"],0)
            self.assertEqual(len(result["monthly"]),3)


if __name__ == "__main__":
    unittest.main()
