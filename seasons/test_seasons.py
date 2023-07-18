from seasons import age_in_minutes, is_date_valid
from datetime import date


def test_valid_dates():
    assert is_date_valid(2000, 8, 3) == True
    assert is_date_valid(1980, 5, 17) == True


def test_invalid_dates():
    assert is_date_valid(2000, 2, 30) == False
    assert is_date_valid(2000, 13, 3) == False
    assert is_date_valid(1989, 10, 41) == False


def test_age_in_minutes():
    t = date.today()
    one_year_ago = date(t.year - 1, t.month, t.day)

    assert age_in_minutes(one_year_ago) == 525600
