import unittest
from datetime import datetime

from financial_projection import completed_months, future_months, month_range, trailing_average


class FinancialProjectionTest(unittest.TestCase):
    def test_completed_year_and_cross_year_forecast(self):
        today=datetime(2026,9,27)
        self.assertEqual(completed_months(2026,today),8)
        self.assertEqual(completed_months(2025,today),12)
        self.assertEqual(future_months(2026,8,6),[(2026,9),(2026,10),(2026,11),(2026,12),(2027,1),(2027,2)])
        self.assertEqual(future_months(2025,12,3),[(2026,1),(2026,2),(2026,3)])
        self.assertEqual(month_range(2024,2),("2024-02-01","2024-02-29"))

    def test_trailing_average_includes_zero_activity_months(self):
        self.assertEqual(trailing_average({6:{"amount":30},8:{"amount":60}},8,"amount"),30)
        self.assertEqual(trailing_average({},0,"amount"),0)


if __name__=="__main__": unittest.main()
