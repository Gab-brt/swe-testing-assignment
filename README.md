# Quick-Calc

Quick-Calc is a simple calculator application developed as part of a Software Testing assignment.  
The goal of this project is not only to implement arithmetic operations, but also to demonstrate a structured testing strategy, proper version control, and continuous integration practices.

---

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Custom handling of division by zero
- Clear (C) functionality
- Command-line interaction layer

---

## Project Structure


swe-testing-assignment/
│
├── quickcalc/ # Core calculator logic
│ ├── calculator.py
│ ├── cli.py
│ ├── errors.py
│ └── init.py
│
├── tests/ # Unit and integration tests
│ ├── test_unit_calculator.py
│ └── test_integration_cli.py
│
├── .github/workflows/ # Continuous Integration configuration
│ └── python-tests.yml
│
├── README.md
├── TESTING.md
└── pyproject.toml


---

## Setup Instructions

1. Clone the repository:


git clone https://github.com/Gab-brt/swe-testing-assignment.git

cd swe-testing-assignment


2. Install pytest:


python -m pip install --upgrade pip
pip install pytest


No additional dependencies are required.

---

## Running the Application

The application logic is separated from the CLI layer.  
You can execute the CLI module directly if needed:


python -m quickcalc.cli


---

## How to Run Tests

All tests can be executed using a single command:


python -m pytest


The test suite includes:
- Unit tests (core logic validation)
- Integration tests (CLI interaction simulation)

Continuous Integration automatically runs these tests on every push to the `main` branch.

---

## Testing Framework Research

Two popular Python testing frameworks were considered for this project: **Unittest** and **Pytest**.

### Unittest
Unittest is the built-in Python testing framework inspired by Java’s JUnit.  
It provides class-based test structures and requires more boilerplate code. While it is stable and widely supported, it tends to be more verbose and less flexible for small projects.

**Advantages:**
- Built into Python (no external dependency)
- Structured, object-oriented approach
- Suitable for large enterprise systems

**Disadvantages:**
- More boilerplate
- Less readable assertions
- Less flexible fixtures system

### Pytest
Pytest is a modern and highly flexible testing framework. It allows simple function-based tests, powerful fixtures, and concise assertions.

**Advantages:**
- Minimal boilerplate
- Powerful fixture system
- Clear and readable assertions
- Automatic test discovery

**Disadvantages:**
- External dependency
- Advanced features may require additional learning

### Final Choice

Pytest was selected because it enables cleaner test definitions, better readability, and easier integration with Continuous Integration workflows. For a project focused on testing strategy and clarity, Pytest provides a more expressive and efficient approach.