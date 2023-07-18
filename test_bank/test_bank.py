from bank import value


def test_value_0():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0


def test_value_20():
    assert value("htop") == 20
    assert value("Htop") == 20
    assert value("HTOP") == 20


def test_value_100():
    assert value("") == 100
