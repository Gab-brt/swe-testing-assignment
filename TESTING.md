# Testing Strategy Documentation

## 1. Overview

This document describes the testing strategy implemented for the Quick-Calc project.  
The objective was not only to verify correctness, but also to apply structured testing principles covered in Lecture 3.

The test suite includes:
- Unit tests (core logic validation)
- Integration tests (interaction between CLI and calculator logic)
- Continuous Integration (automated execution on every push)

---

## 2. Testing Strategy

### What was tested

The following components were tested:

- Arithmetic operations (add, subtract, multiply, divide)
- Division by zero handling
- Session state reset (clear functionality)
- CLI interaction sequences
- Edge cases (negative numbers, decimal values)

### What was not tested

The following aspects were intentionally not tested:

- Performance under heavy computational load
- Concurrency behavior
- Security-related aspects
- User interface aesthetics

The project focuses primarily on functional correctness rather than non-functional requirements.

---

## 3. Lecture Concepts Applied

### 3.1 Testing Pyramid

The project follows the Testing Pyramid principle:

- Most tests are unit tests (8 tests)
- Fewer integration tests (3 tests)
- No end-to-end UI automation

This reflects the pyramid model:
- Unit tests are fast, isolated, and numerous
- Integration tests validate interactions
- High-level tests are limited to avoid fragility

This structure ensures fast feedback and maintainability.

---

### 3.2 Black-box vs White-box Testing

**Unit tests** are partially white-box tests because they directly test internal functions (add, subtract, divide).

**Integration tests** are closer to black-box testing since they simulate user input sequences without relying on internal implementation details.

This mixed approach ensures:
- Internal correctness (white-box)
- External behavior validation (black-box)

---

### 3.3 Functional vs Non-Functional Testing

The current test suite focuses on **functional testing**:
- Verifying correct mathematical outputs
- Ensuring error handling works as expected

Non-functional aspects such as performance, scalability, and usability were not part of the project scope.

---

### 3.4 Regression Testing

The test suite acts as a regression safety net.

If future modifications introduce errors (e.g., breaking division logic or CLI behavior), the automated test suite and CI workflow will immediately detect failures.

Continuous Integration ensures that every push is automatically validated, preventing unstable versions from being released.

---

## 4. Test Results Summary

| Test Name | Type | Status |
|-----------|------|--------|
| test_addition | Unit | Pass |
| test_subtraction | Unit | Pass |
| test_multiplication | Unit | Pass |
| test_division | Unit | Pass |
| test_division_by_zero | Unit | Pass |
| test_negative_numbers | Unit | Pass |
| test_decimal_numbers | Unit | Pass |
| test_clear_resets_session | Unit | Pass |
| test_full_user_interaction_addition | Integration | Pass |
| test_clear_after_calculation_resets_result | Integration | Pass |
| test_division_by_zero_is_handled | Integration | Pass |

All tests pass successfully in local execution and in the CI pipeline.

---

## 5. Conclusion

The testing approach combines:
- Structured unit testing
- Controlled integration testing
- Automated CI validation

This ensures reliability, maintainability, and protection against regressions, while remaining aligned with the principles discussed in Lecture 3.