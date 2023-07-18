from jar import Jar
import pytest


def test_init():
    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0


def test_deposit():
    jar = Jar(5)
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(2)
    assert jar.size == 3
    with pytest.raises(ValueError):
        assert jar.deposit(6)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(4)
    assert str(jar) == "🍪🍪🍪🍪🍪"


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(2)
    assert jar.size == 8
    jar.withdraw(8)
    assert jar.size == 0
    with pytest.raises(ValueError):
        assert jar.withdraw(1)
