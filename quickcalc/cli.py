from __future__ import annotations

from .calculator import add, subtract, multiply, divide, CalculatorSession


def run_sequence(tokens: list[str]) -> float:
    """
    Simulates a simple calculator interaction using a list of tokens.

    Example:
        ["5", "+", "3", "="] -> 8

    Supported tokens:
        - numbers (e.g., "5", "3.2", "-7")
        - operators: "+", "-", "*", "/"
        - "C" for clear
        - "=" to return the current result
    """

    session = CalculatorSession()
    pending_operation: str | None = None

    for token in tokens:
        token = token.strip()

        # Handle clear command
        if token.upper() == "C":
            session.clear()
            pending_operation = None
            continue

        # Store the selected operation
        if token in {"+", "-", "*", "/"}:
            pending_operation = token
            continue

        # Return current result when "=" is pressed
        if token == "=":
            return session.result

        # Convert numeric token to float
        value = float(token)

        # First value initialization
        if session.result == 0.0 and pending_operation is None and session.current_input == 0.0:
            session.result = value
            session.current_input = value
            continue

        # If no operation is pending, replace current result
        if pending_operation is None:
            session.result = value
            session.current_input = value
            continue

        # Apply the selected operation
        if pending_operation == "+":
            session.result = add(session.result, value)
        elif pending_operation == "-":
            session.result = subtract(session.result, value)
        elif pending_operation == "*":
            session.result = multiply(session.result, value)
        elif pending_operation == "/":
            session.result = divide(session.result, value)

        session.current_input = value
        pending_operation = None

    return session.result
