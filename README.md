# BIT Gym Membership Management System

**Course:** PRG1406 — Advanced Programming (Python and C)  
**Institution:** Burkina Institute of Technology  
**Assignment:** Group Assignment 1 — May 2026  

---

## Group Members

| fullname |
|------|
| OUEDRAOGO Bowend-yaam Esther |
| NIKIEMA Flora Inès |
| COMPAORE Salamata |
| KIENDREBEOGO Moussa |
| ZOUNGRANA Zalissa |

---

## What the Program Does

This program simulates a **Gym Membership Management System**. It collects information about two gym members (one regular, one premium), validates all input, calculates BMI and costs, and displays a formatted summary report.

It demonstrates:

- All four Python data types used meaningfully (`str`, `int`, `float`, `bool`)
- Correct input validation with `while` + `try/except`
- Object-Oriented Programming with inheritance
- Magic (dunder) methods: `__str__`, `__eq__`, `__len__`
- Python decorators: `@staticmethod`, `@classmethod`, `@property`

---

## Classes

### `Member` — Parent Class

Represents a standard gym member.

| Feature | Detail |
|--------|--------|
| Attributes | `name` (str), `age` (int), `weight` (float), `height` (float), `is_active` (bool) |
| Magic methods | `__str__`, `__eq__`, `__len__` |
| Decorators | `@staticmethod calculate_bmi()`, `@classmethod get_total_members()` |

### `PremiumMember(Member)` — Child Class

A `PremiumMember` **IS A** `Member` with extra features. Uses `super().__init__()` to call the parent constructor.

| Feature | Detail |
|--------|--------|
| Extra attributes | `trainer_name` (str), `monthly_fee` (float), `sessions_per_week` (int) |
| Decorator | `@property yearly_cost` — computed from `monthly_fee * 12` |
| Overrides | `__str__` (adds premium details), `__len__` (returns sessions/week) |

---

## How to Run

```bash
python gym_management.py
```

**Requirements:** Python 3.13 or higher. No external packages needed.

---

## Example Interaction

```
====================================================
   BIT GYM MEMBERSHIP MANAGEMENT SYSTEM
   PRG1406 -- Group Assignment 1
====================================================

  REGISTER REGULAR MEMBER
  Full name           : Zalissa NIKIEMA
  Age (years)         : 28
  Weight (kg)         : 72.5
  Height (m, e.g 1.75): 1.78
  Active member? (yes/no): yes

  REGISTER PREMIUM MEMBER
  Full name           : Moussa KIENDREBEOGO
  Age (years)         : 30
  Weight (kg)         : 80.0
  Height (m, e.g 1.80): 1.82
  Active member? (yes/no): yes
  Trainer's name      : Coach Ibrahim
  Monthly fee ($)     : 45.00
  Sessions per week   : 4

  ...

  ================================================
           MEMBERSHIP SUMMARY REPORT
  ================================================
  Total members registered : 2
  ...
  Program completed successfully. No errors.
```

---

## Project Structure

```
.
├── gym_management.py   # Main program
└── README.md           # This file
```
