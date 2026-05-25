# Test Run Report — PRG1406 Group 8 Assignment 1
**Student:** ZOUNGRANA Zalissa  
**Task:** Tests and Final Verification  
**Date:** 2026-05-25  
**File tested:** `gym_management.py`  
**Python version:** Python 3.x  

---

## Test Cases

| # | Test Description | Expected Result | Actual Result | Status |
|---|-----------------|-----------------|---------------|--------|
| 1 | Create `Member` object (ALICE OUEDRAOGO) | Object created with correct attributes | Object created successfully | ✅ PASS |
| 2 | Create `PremiumMember` object (OUEDRAOGO ESTHER) | Inherits from `Member`, extra attributes set | Inheritance working correctly | ✅ PASS |
| 3 | BMI calculation for regular member | 21.87 (Normal weight) | 21.87 — Normal weight | ✅ PASS |
| 4 | BMI calculation for premium member | 37.19 | 37.19 displayed correctly | ✅ PASS |
| 5 | Membership summary report | All fields displayed correctly | All fields printed correctly | ✅ PASS |
| 6 | Magic methods `__str__`, `__len__`, `__eq__` | Correct output for all three | All three returned correct values | ✅ PASS |
| 7 | Decorators `@staticmethod`, `@classmethod`, `@property` | All return correct values | All returned correct values | ✅ PASS |
| 8 | Run full program, no exceptions | Exits cleanly with no errors | "Program completed successfully. No errors." | ✅ PASS |
| 9 | Active status: invalid input `"BANANA"` (ALICE) | Non-"yes" input → `False` → Inactive | Status: Inactive | ✅ PASS |
| 10 | Active status: empty input / Enter key (ESTHER) | Empty input → `False` → Inactive | Status: Inactive | ✅ PASS |

---

### Note on Tests 9 & 10 — Boolean Principle

The `is_active` field uses a strict boolean check:
```python
self.is_active = active_input.lower() == "yes"
```
Any input that is not exactly `"yes"` (including `"BANANA"`, empty string, `"no"`, etc.)
evaluates to `False` and sets the member as **Inactive**.
The program does not print a warning for invalid input — it silently defaults to `False`.
This behavior is correct and the boolean logic works as expected.

---

## Program Output
