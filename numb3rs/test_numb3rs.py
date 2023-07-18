from numb3rs import validate


def test_not_ipv4():
    assert validate("this isn't an ip address") == False
    assert validate("2345:0425:2CA1:0000:0000:0567:5673:23b5") == False


def test_invalid_ipv4():
    assert validate("275.0.5.6") == False
    assert validate("189.300.10.1") == False


def test_valid_ipv4():
    assert validate("192.168.1.100") == True
    assert validate("10.0.0.1") == True
    assert validate("179.50.32.255") == True
