import pytest
import fuel


def test_gauge():
    assert fuel.gauge(0) == "E"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(100) == "F"
    assert fuel.gauge(50) == "50%"


def test_convert():
    assert fuel.convert("1/2") == 50
    assert fuel.convert("1/4") == 25
    assert fuel.convert("1/100") == 1
    assert fuel.convert("1/1") == 100
    with pytest.raises(ValueError):
        assert fuel.convert("3/2")
        assert fuel.convert("cat/dog")
        assert fuel.convert("nope")
    with pytest.raises(ZeroDivisionError):
        assert fuel.convert("2/0")
