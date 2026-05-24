# Part 4 — Decorators
**Prepared by:** KIENDREBEOGO Moussa  
**Course:** PRG1406 — Advanced Programming (Python and C)  
**Burkina Institute of Technology — May 2026**

---

## What is a Decorator?

A **decorator** is a special symbol (`@`) placed above a function or method that **modifies its behaviour** without changing its internal code.

```python
@decorator_name
def my_function():
    ...
```

Python has three built-in decorators for class methods:
- `@staticmethod`
- `@classmethod`
- `@property`

All three are used in our program.

---

## 1. `@staticmethod` — `calculate_bmi()`

```python
@staticmethod
def calculate_bmi(weight: float, height: float) -> float:
    return weight / (height ** 2)
```

### What it does:
- Belongs to the **class**, not to any specific instance
- Does **not** receive `self` or `cls`
- Can be called without creating an object

### How to call it:
```python
bmi = Member.calculate_bmi(72.5, 1.78)
# → 22.87
```

### Why use it here?
BMI is a pure mathematical formula. It does not need any information about a specific member — just weight and height. So it makes sense as a static method.

### Key rule:
> Use `@staticmethod` when the method does **not need** access to the instance (`self`) or the class (`cls`).

---

## 2. `@classmethod` — `get_total_members()`

```python
@classmethod
def get_total_members(cls) -> int:
    return cls.total_members
```

### What it does:
- Receives the **class itself** as the first argument (`cls`)
- Can access and modify **class-level variables** (shared across all instances)
- Called on the class, not on an instance

### How to call it:
```python
count = Member.get_total_members()
# → 2  (after registering 2 members)
```

### How `total_members` works:
```python
class Member:
    total_members = 0  # shared by ALL Member objects

    def __init__(self, ...):
        Member.total_members += 1  # increments every time a new member is created
```

Every time a `Member` or `PremiumMember` is created, `total_members` increases by 1.  
`get_total_members()` reads that shared counter.

### Key rule:
> Use `@classmethod` when the method needs access to the **class itself** or **class-level data**.

---

## 3. `@property` — `yearly_cost`

```python
@property
def yearly_cost(self) -> float:
    return self.monthly_fee * 12
```

### What it does:
- Makes a method **behave like an attribute**
- No parentheses needed when accessing it
- Computes a value **dynamically** each time it is accessed

### How to access it:
```python
# Correct — no parentheses
print(premium1.yearly_cost)   # → 540.00

# Wrong — do not add parentheses
print(premium1.yearly_cost()) # → TypeError!
```

### Why use it here?
`yearly_cost` depends on `monthly_fee`. Instead of storing it as a fixed attribute (which could become outdated if `monthly_fee` changes), we compute it on the fly with `@property`.

If `monthly_fee = 45.00`, then `yearly_cost = 45.00 * 12 = 540.00`.  
If `monthly_fee` changes to `60.00`, `yearly_cost` automatically becomes `720.00` — no manual update needed.

### Key rule:
> Use `@property` when a value should be **computed dynamically** from other attributes and accessed like an attribute (without parentheses).

---

## Comparison Table

| Decorator | First argument | How to call | Use case |
|-----------|---------------|-------------|----------|
| `@staticmethod` | nothing | `Class.method(args)` | Pure utility functions with no class/instance data |
| `@classmethod` | `cls` (the class) | `Class.method()` | Access or modify class-level data |
| `@property` | `self` (the instance) | `object.attribute` | Computed attributes, accessed without `()` |

---

## Live Demo from the Program

```python
# @staticmethod — called directly on the class
Member.calculate_bmi(80.0, 1.82)
# → 24.15

# @classmethod — returns the shared counter
Member.get_total_members()
# → 2

# @property — accessed like an attribute, no parentheses
premium1.yearly_cost
# → 540.00
```

---

## Summary

Decorators are a powerful Python feature that change how methods behave:

- `@staticmethod` → utility method, no instance or class needed
- `@classmethod` → works with class-level data using `cls`
- `@property` → turns a method into a readable attribute
