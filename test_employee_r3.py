"""Employee registration fields must survive edits and upgrades of company files."""
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from database import Database
from payroll_reports import build_nssf_statement


class EmployeeRegistrationTest(unittest.TestCase):
    def test_registration_fields_are_saved_and_preserved_on_edit(self):
        with TemporaryDirectory() as folder:
            db = Database(Path(folder) / "company.db")
            db.initialize("secret12345")
            with db.connect() as connection:
                user_id = connection.execute("SELECT id FROM users WHERE username='admin'").fetchone()[0]
            employee = db.save_employee({"full_name": "Maya Haddad", "nationality": "Lebanese",
                "father_name": "Joseph", "mother_name": "Lina", "birth_date": "15-06-1992",
                "birth_place": "Jounieh"}, user_id)
            self.assertEqual(employee["birth_date"], "1992-06-15")
            updated = db.save_employee({**employee, "nationality": "French"}, user_id)
            self.assertEqual(updated["nationality"], "French")
            self.assertEqual(updated["mother_name"], "Lina")
            db.initialize("secret12345")
            self.assertEqual(db.list_employees()[0]["birth_place"], "Jounieh")

    def test_nssf_roster_counts_employees_without_payroll(self):
        with TemporaryDirectory() as folder:
            db = Database(Path(folder) / "company.db")
            db.initialize("secret12345")
            with db.connect() as connection:
                user_id = connection.execute("SELECT id FROM users WHERE username='admin'").fetchone()[0]
            for number in ("100000001", "100000002"):
                db.save_employee({"employee_number": number, "full_name": "Same Name",
                                  "hire_date": "01-01-2025"}, user_id)
            report = build_nssf_statement(db, "yearly", 2025)
            self.assertEqual(report["employee_count"], 2)
            self.assertEqual(report["payroll_employee_count"], 0)
            self.assertEqual(len(report["sections"][1]["rows"]), 2)


if __name__ == "__main__":
    unittest.main()
