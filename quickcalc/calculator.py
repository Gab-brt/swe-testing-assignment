from .errors import DivisionByZeroError


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise DivisionByZeroError("Division by zero is not allowed.")
    return a / b


class CalculatorSession:
    """
    Stateful calculator session to support Clear (C) behavior.
    """
    def __init__(self) -> None:
        self.current_input = 0.0
        self.result = 0.0

    def clear(self) -> None:
        self.current_input = 0.0
        self.result = 0.0
