from math_series.series import fibo
from math_series.series import lucas
from math_series.series import sum_series

def test_fibonacci_five():
    assert fibo(5) == 5

def test_fibonacci_two():
    assert fibo(2) == 1


def test_fibonacci_three3():
    assert fibo(3) == 2


def test_fibonacci_seven():
    assert fibo(7) == 13


def test_lucas_zero():
    assert lucas(0) == 2

def test_lucas_three():
    assert lucas(3) == 4


def test_lucas_seven():
    assert lucas(7) == 29


def test_sum_series():
    assert sum_series(3, 4, 2) == 8


def test_sum_series():
    assert sum_series(3, 4, 1) == 6