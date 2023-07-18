from working import convert
import pytest


def test_valid_input():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("5:00 PM to 9:00 AM") == "17:00 to 09:00"


def test_invalid_input_format():
    with pytest.raises(ValueError):
        assert convert("9:00AM to 5:00PM")
    with pytest.raises(ValueError):
        assert convert("9:00 am to 5:00 pm")
    with pytest.raises(ValueError):
        assert convert("9 to 5")
    with pytest.raises(ValueError):
        assert convert("9 5")


def test_invalid_time():
    with pytest.raises(ValueError):
        assert convert("13:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        assert convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        assert convert("9:00 AM to 13:00 PM")
