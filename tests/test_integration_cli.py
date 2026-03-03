import pytest
from quickcalc.cli import run_sequence
from quickcalc.errors import DivisionByZeroError


def test_full_user_interaction_addition():
    """
    Simulates a complete user interaction:
    User enters 5, presses '+', enters 3, and presses '='.
    The expected result is 8.
    """
    result = run_sequence(["5", "+", "3", "="])
    assert result == 8


def test_clear_after_calculation_resets_result():
    """
    After performing a calculation, pressing 'C'
    should reset the calculator result to 0.
    """
    result = run_sequence(["5", "+", "3", "C", "="])
    assert result == 0.0


def test_division_by_zero_is_handled():
    """
    Division by zero should raise the custom
    DivisionByZeroError exception.
    """
    with pytest.raises(DivisionByZeroError):
        run_sequence(["10", "/", "0", "="])
