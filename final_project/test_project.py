from project import timestamp_to_date, format_to_brl, array_to_data_frame
from datetime import date
import pandas as pd


def test_format_to_brl():
    assert format_to_brl(15000) == "R$ 15,00 K"
    assert format_to_brl(1500000) == "R$ 1,50 Mi"
    assert format_to_brl(1500000000) == "R$ 1,50 Bi"
    assert format_to_brl(1500000000000) == "R$ 1,50 Tri"


def test_timestamp_to_date():
    assert timestamp_to_date(0) == date(1970, 1, 1)
    assert timestamp_to_date(1609459200) == date(2021, 1, 1)
    assert timestamp_to_date(1640995200) == date(2022, 1, 1)
    assert timestamp_to_date(1672531200) == date(2023, 1, 1)
    assert timestamp_to_date(1704067200) == date(2024, 1, 1)


def test_array_to_data_frame():
    arr = [
        {
            "date": date(2023, 7, 12),
            "open": 9.619999885559082,
            "high": 9.670000076293945,
            "low": 9.539999961853027,
            "close": 9.600000381469727,
            "volume": 10093000,
            "adjustedClose": 9.600000381469727,
        },
        {
            "date": date(2023, 7, 13),
            "open": 9.609999656677246,
            "high": 9.8100004196167,
            "low": 9.550000190734863,
            "close": 9.720000267028809,
            "volume": 13337800,
            "adjustedClose": 9.720000267028809,
        },
    ]
    test_data = [
        {
            "date": 1689166800,
            "open": 9.619999885559082,
            "high": 9.670000076293945,
            "low": 9.539999961853027,
            "close": 9.600000381469727,
            "volume": 10093000,
            "adjustedClose": 9.600000381469727,
        },
        {
            "date": 1689253200,
            "open": 9.609999656677246,
            "high": 9.8100004196167,
            "low": 9.550000190734863,
            "close": 9.720000267028809,
            "volume": 13337800,
            "adjustedClose": 9.720000267028809,
        },
    ]
    valid_df = pd.DataFrame(arr)
    valid_df = valid_df.set_index("date")

    assert array_to_data_frame(test_data).equals(valid_df)
