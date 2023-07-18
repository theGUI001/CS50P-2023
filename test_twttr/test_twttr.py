import pytest
from twttr import shorten


def test_shorten_lower():
    assert shorten("twitter") == "twttr"
    assert shorten("abcdefghi") == "bcdfgh"
    assert shorten("e") == ""
    assert shorten("b") == "b"


def test_shorten_upper():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("ABCDEFGHI") == "BCDFGH"
    assert shorten("E") == ""
    assert shorten("B") == "B"


def test_shorten_null():
    with pytest.raises(TypeError):
        shorten()


def test_shorten_empty_string():
    assert shorten("") == ""


def test_shorten_numbers():
    with pytest.raises(TypeError):
        shorten(12)
    assert shorten("123") == "123"


def test_shorten_punctuation():
    assert shorten(",.;") == ",.;"
