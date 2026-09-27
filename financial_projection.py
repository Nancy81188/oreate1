"""Small, explicit forecasts from complete monthly accounting periods."""
import calendar
from datetime import datetime

HORIZONS = {"Quarter (3 months)": 3, "6 Months": 6, "Yearly (12 months)": 12}


def completed_months(year, now=None):
    today = now or datetime.now()
    if year > today.year:
        raise ValueError("Choose this year or an earlier report year")
    return 12 if year < today.year else today.month - 1


def month_range(year, month):
    end = calendar.monthrange(year, month)[1]
    return f"{year}-{month:02d}-01", f"{year}-{month:02d}-{end:02d}"


def future_months(year, last, count):
    if count not in HORIZONS.values():
        raise ValueError("Choose Quarter, 6 Months, or Yearly")
    return [((year * 12 + last - 1 + offset) // 12,
             (year * 12 + last - 1 + offset) % 12 + 1) for offset in range(1, count + 1)]


def trailing_average(monthly, last, field, window=3):
    months = range(max(1, last - window + 1), last + 1)
    return sum(float(monthly.get(month, {}).get(field, 0)) for month in months) / len(months) if last else 0.0
