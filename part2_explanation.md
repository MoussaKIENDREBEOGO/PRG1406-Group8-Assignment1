# Part 2 – Inheritance (Héritage) in Python
**PRG1406 – Advanced Programming (Python and C)**
**Burkina Institute of Technology – CS27 Program**
**Group 8 – Assignment 1**

---

## 1. What is Inheritance?

Inheritance is one of the four fundamental principles of Object-Oriented Programming (OOP). It allows a **child class** (also called a subclass or derived class) to **inherit attributes and methods** from a **parent class** (also called a superclass or base class).

This mechanism promotes **code reuse**, **modularity**, and **extensibility**: instead of rewriting shared logic, the child class inherits it automatically and can extend or override it as needed.

**General syntax in Python:**

```python
class ParentClass:
    # attributes and methods of the parent
    pass

class ChildClass(ParentClass):
    # inherits everything from ParentClass
    # can add new attributes/methods or override existing ones
    pass
```

---

## 2. Application: Gym Management System (`gym_management.py`)

Our program implements a gym membership management system using two classes that illustrate single inheritance:

- **`Member`** — the parent class representing a standard gym member.
- **`PremiumMember`** — the child class representing a member with a premium subscription.

---

## 3. The Parent Class: `Member`

The `Member` class defines the **common attributes and behaviours** shared by all gym members.

```python
class Member:
    def __init__(self, name, age, membership_id):
        self.name = name
        self.age = age
        self.membership_id = membership_id

    def display_info(self):
        print(f"Member: {self.name}, Age: {self.age}, ID: {self.membership_id}")

    def check_in(self):
        print(f"{self.name} has checked in.")
```

**Key attributes:**
- `name` – the member's full name
- `age` – the member's age
- `membership_id` – a unique identifier for the member

**Key methods:**
- `display_info()` – displays the member's basic information
- `check_in()` – records a gym visit

---

## 4. The Child Class: `PremiumMember`

The `PremiumMember` class **inherits** from `Member` and extends it with premium-specific features.

```python
class PremiumMember(Member):
    def __init__(self, name, age, membership_id, personal_trainer):
        super().__init__(name, age, membership_id)
        self.personal_trainer = personal_trainer

    def display_info(self):
        super().display_info()
        print(f"Personal Trainer: {self.personal_trainer}")

    def book_session(self):
        print(f"{self.name} has booked a session with trainer {self.personal_trainer}.")
```

---

## 5. Key Inheritance Concepts Demonstrated

### 5.1 The `super()` Function

The `super()` function is used to call a method from the **parent class** within the child class. In `PremiumMember.__init__()`, it initialises the inherited attributes (`name`, `age`, `membership_id`) without duplicating code:

```python
super().__init__(name, age, membership_id)
```

This is the recommended way to ensure the parent class is properly initialised before adding child-specific logic.

### 5.2 Method Overriding

`PremiumMember` **overrides** the `display_info()` method inherited from `Member`. Instead of replacing the parent's logic entirely, it calls `super().display_info()` first and then adds the trainer information:

```python
def display_info(self):
    super().display_info()          # calls the parent's version
    print(f"Personal Trainer: {self.personal_trainer}")
```

This is a best practice: it extends rather than replaces the parent's behaviour.

### 5.3 Adding New Attributes and Methods

The child class introduces:
- A new attribute: `personal_trainer`
- A new method: `book_session()` — not available in the parent class

This demonstrates how inheritance allows **specialisation** without modifying the parent class.

### 5.4 Inherited Methods Used Without Redefinition

The `check_in()` method defined in `Member` is **automatically available** in `PremiumMember` without any additional code. A `PremiumMember` object can call `check_in()` directly:

```python
pm = PremiumMember("Alice", 28, "PM-001", "Coach Kader")
pm.check_in()  # Output: Alice has checked in.
```

---

## 6. Inheritance Hierarchy Diagram

```
        ┌──────────────────────────┐
        │         Member           │
        │--------------------------|
        │ + name                   │
        │ + age                    │
        │ + membership_id          │
        │--------------------------|
        │ + display_info()         │
        │ + check_in()             │
        └────────────┬─────────────┘
                     │
              inherits (↓)
                     │
        ┌────────────▼─────────────┐
        │      PremiumMember       │
        │--------------------------|
        │ + personal_trainer       │  ← new attribute
        │--------------------------|
        │ + display_info()         │  ← overridden
        │ + book_session()         │  ← new method
        │ + check_in()             │  ← inherited as-is
        └──────────────────────────┘
```

---

## 7. Benefits of Using Inheritance Here

| Benefit | How it applies in our program |
|---|---|
| **Code Reuse** | `PremiumMember` reuses `name`, `age`, `membership_id`, `check_in()` from `Member` without rewriting them |
| **Extensibility** | New member types (e.g., `StudentMember`, `SeniorMember`) can be created from `Member` easily |
| **Maintainability** | Changes to shared logic in `Member` automatically apply to all subclasses |
| **Polymorphism** | Both `Member` and `PremiumMember` objects can call `display_info()`, with each producing appropriate output |

---

## 8. Conclusion

This program demonstrates **single inheritance** in Python through a practical gym management context. The `Member` class encapsulates common member data and behaviour, while `PremiumMember` extends it to support premium-specific features. The use of `super()`, method overriding, and new method definitions illustrates the core mechanics of inheritance in an applied and readable way.

---

*Prepared by: NIKIEMA Flora Inès – Group 8, CS27 – BIT, May 2026*
