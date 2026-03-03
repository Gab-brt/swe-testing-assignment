import pytest
from quickcalc.calculator import add, subtract, multiply, divide, CalculatorSession
from quickcalc.errors import DivisionByZeroError


def test_addition():
    """Addition of two positive numbers."""
    assert add(5, 3) == 8


def test_subtraction():
    """Subtraction of two positive numbers."""
    assert subtract(10, 4) == 6


def test_multiplication():
    """Multiplication of two positive numbers."""
    assert multiply(6, 7) == 42


def test_division():
    """Division of two positive numbers."""
    assert divide(8, 2) == 4


def test_division_by_zero():
    """Division by zero should raise a custom exception."""
    with pytest.raises(DivisionByZeroError):
        divide(10, 0)


def test_negative_numbers():
    """Operations should handle negative values correctly."""
    assert add(-5, 2) == -3


def test_decimal_numbers():
    """Floating point addition should be approximately correct."""
    assert add(0.1, 0.2) == pytest.approx(0.3)


def test_clear_resets_session():
    """Clear method should reset session state to zero."""
    session = CalculatorSession()
    session.current_input = 99
    session.result = 42
    session.clear()
    assert session.current_input == 0.0
    assert session.result == 0.0