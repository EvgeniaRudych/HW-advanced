import pytest
from Calc import Calculator


def test_add():
    assert Calculator.add(1, 2) == 3
    assert Calculator.add(-3, -2) == -5
    with pytest.raises(TypeError):
        Calculator.add('a', 3)


def test_subtract():
    assert Calculator.subtrast(1, 1) == 0
    assert Calculator.subtract(-8, 5) == -13
    assert Calculator.subtract(5, 7) != 1
    with pytest.raises(TypeError):
        Calculator.subtract('q', 2)


def test_multiply():
    assert Calculator.multiply(3, 3) == 9
    assert Calculator.multiply('a', 4) == 'aaaa'
    assert Calculator.multiply(2, 3) != 2


def test_divide():
    assert Calculator.divide(4, 2) == 2
    assert Calculator.divide(-2, -2) == 1
    assert Calculator.divide(4, 1) != 3
    with pytest.raises(ValueError):
        Calculator.divide(1, 0)
        Calculator.divide(3.4, 0)
    with pytest.raises(TypeError):
        Calculator.divide('r', 2)
        Calculator.divide({1, 2, 3}, 3)



