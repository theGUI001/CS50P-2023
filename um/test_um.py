from um import count


def test_count_basic():
    assert count("hello, um, world") == 1
    assert count("yummy") == 0


def test_count_case_insensitive():
    assert count("Um, excuse me") == 1
    assert count("UM, EXCUSE ME") == 1


def test_count_multiple():
    assert count("um, um, um") == 3
