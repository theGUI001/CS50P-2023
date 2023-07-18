from plates import is_valid


def test_is_valid_less_2():
    assert is_valid("A") == False
    assert is_valid("b") == False


def test_is_valid_more_6():
    assert is_valid("AAAAAAA") == False
    assert is_valid("bbbbbbb") == False
    assert is_valid("cccCCCC") == False


def test_is_valid_special_char():
    assert is_valid("Ab#01") == False
    assert is_valid("CA$H") == False


def test_is_valid_numbers():
    assert is_valid("1234") == False
    assert is_valid("123AbC") == False
    assert is_valid("CS50P") == False


def test_is_valid_valid_plates():
    assert is_valid("CS50") == True
    assert is_valid("PLATE") == True
    assert is_valid("abc123") == True
    assert is_valid("HM") == True


def test_is_valid_zero():
    assert is_valid("CS05") == False
