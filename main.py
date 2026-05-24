# ============================================================
#  main.py
#  BIT Gym Membership Management System
#  PRG1406 - Advanced Programming (Python and C)
#  Group Assignment 1 - May 2026
#
#  Group 8:
#    - KIENDREBEOGO Moussa
#    - OUEDRAOGO Esther
#    - ZOUNGRANA Zalissa
#    - NIKIEMA Ines
#    - COMPAORE Salimata
# ============================================================

from classes import Member, PremiumMember


# ------------------------------------------------------------
#  PART 1 - Input validation helpers
#  Each function uses: while loop + try/except
#  Re-prompts the user on bad input, never crashes
# ------------------------------------------------------------

def get_int(prompt: str, min_val: int = 1) -> int:
    """
    Reads and validates an integer from the user.
    Keeps asking until a valid integer >= min_val is entered.

    Example: age = get_int("Enter age: ", min_val=1)
    """
    while True:
        try:
            value = int(input(prompt))
            if value < min_val:
                print(f"  ⚠  Value must be at least {min_val}. Try again.")
                continue
            return value
        except ValueError:
            print("  ⚠  Please enter a whole number (e.g. 25).")


def get_float(prompt: str, min_val: float = 0.01) -> float:
    """
    Reads and validates a float from the user.
    Keeps asking until a valid float >= min_val is entered.

    Example: weight = get_float("Enter weight (kg): ")
    """
    while True:
        try:
            value = float(input(prompt))
            if value < min_val:
                print(f"  ⚠  Value must be greater than {min_val}. Try again.")
                continue
            return value
        except ValueError:
            print("  ⚠  Please enter a decimal number (e.g. 70.5).")


def get_str(prompt: str) -> str:
    """
    Reads and validates a non-empty string from the user.
    Keeps asking until the user types something.

    Example: name = get_str("Enter full name: ")
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  ⚠  This field cannot be empty. Try again.")


# ------------------------------------------------------------
#  Main Program
# ------------------------------------------------------------

def main():

    # -- Welcome banner --
    print("\n" + "=" * 52)
    print("    BIT GYM MEMBERSHIP MANAGEMENT SYSTEM")
    print("    PRG1406 -- Group 8 -- Assignment 1")
    print("=" * 52)

    # --------------------------------------------------------
    #  REGISTER A REGULAR MEMBER
    #  Part 1: 5 input() calls with type casting + correct bool
    # --------------------------------------------------------
    print("\n  ── REGISTER REGULAR MEMBER ──────────────────")

    # str input
    name1 = get_str("  Full name             : ")

    # int input with casting
    age1 = get_int("  Age (years)           : ", min_val=5)

    # float input with casting
    weight1 = get_float("  Weight (kg)           : ", min_val=1.0)

    # float input with casting
    height1 = get_float("  Height (m, e.g. 1.75) : ", min_val=0.5)

    # PART 1: correct boolean - comparing string, NOT bool(input(...))
    is_active1: bool = input("  Active member? (yes/no): ").strip().lower() == "yes"

    # Create the regular member object
    member1 = Member(name1, age1, weight1, height1, is_active1)

    print(f"\n  ✔  Regular member '{name1}' registered successfully.")

    # --------------------------------------------------------
    #  REGISTER A PREMIUM MEMBER
    #  Part 1: 8 more input() calls (total = 13 inputs)
    # --------------------------------------------------------
    print("\n  ── REGISTER PREMIUM MEMBER ──────────────────")

    # str input
    name2 = get_str("  Full name             : ")

    # int input with casting
    age2 = get_int("  Age (years)           : ", min_val=5)

    # float input with casting
    weight2 = get_float("  Weight (kg)           : ", min_val=1.0)

    # float input with casting
    height2 = get_float("  Height (m, e.g. 1.80) : ", min_val=0.5)

    # PART 1: correct boolean
    is_active2: bool = input("  Active member? (yes/no): ").strip().lower() == "yes"

    # str input
    trainer = get_str("  Trainer's name        : ")

    # float input with casting
    fee = get_float("  Monthly fee ($)       : ", min_val=1.0)

    # int input with casting
    sessions = get_int("  Sessions per week     : ", min_val=1)

    # Create the premium member object
    premium1 = PremiumMember(name2, age2, weight2, height2,
                              is_active2, trainer, fee, sessions)

    print(f"\n  ✔  Premium member '{name2}' registered successfully.")

    # --------------------------------------------------------
    #  PART 1 - Arithmetic expressions
    # --------------------------------------------------------
    bmi1            = Member.calculate_bmi(weight1, height1)   # expression 1
    bmi2            = Member.calculate_bmi(weight2, height2)   # expression 2
    total_yearly    = premium1.yearly_cost                      # expression 3 (via @property)
    weekly_calories = 450 * sessions                            # expression 4
    cost_per_session = fee / (sessions * 4) if sessions > 0 else 0  # expression 5

    # --------------------------------------------------------
    #  SUMMARY SCREEN
    #  Part 1: f-strings for ALL output
    # --------------------------------------------------------
    print("\n\n" + "=" * 52)
    print("          MEMBERSHIP SUMMARY REPORT")
    print("=" * 52)

    print(f"\n  Total members registered : {Member.get_total_members()}")

    # -- Regular member summary --
    print(f"\n  REGULAR MEMBER - {name1.upper()}")
    member1.display_info()

    print(f"  BMI Classification : ", end="")
    if   bmi1 < 18.5: print("Underweight")
    elif bmi1 < 25.0: print("Normal weight")
    elif bmi1 < 30.0: print("Overweight")
    else:             print("Obese")

    # -- Premium member summary --
    print(f"\n  PREMIUM MEMBER - {name2.upper()}")
    premium1.display_premium_info()

    # --------------------------------------------------------
    #  MAGIC METHODS DEMO - Part 3
    # --------------------------------------------------------
    print("  ── MAGIC METHODS DEMO (Part 3) ──────────────")
    print(f"  print(member1)        -> {member1}")
    print(f"  print(premium1)       -> {premium1}")
    print(f"  len(member1)          -> {len(member1)}  (age in years)")
    print(f"  len(premium1)         -> {len(premium1)}  (sessions per week)")
    print(f"  member1 == premium1   -> {member1 == premium1}")

    # --------------------------------------------------------
    #  DECORATORS DEMO - Part 4
    # --------------------------------------------------------
    print(f"\n  ── DECORATORS DEMO (Part 4) ─────────────────")
    print(f"  @staticmethod")
    print(f"    Member.calculate_bmi({weight2}, {height2})")
    print(f"    = {Member.calculate_bmi(weight2, height2):.2f}")
    print(f"\n  @classmethod")
    print(f"    Member.get_total_members()")
    print(f"    = {Member.get_total_members()}")
    print(f"\n  @property")
    print(f"    premium1.yearly_cost")
    print(f"    = ${premium1.yearly_cost:.2f}")

    # --------------------------------------------------------
    #  FINAL SUMMARY - f-strings (Part 1)
    # --------------------------------------------------------
    print(f"\n  {'=' * 48}")
    print(f"  FINAL REPORT")
    print(f"  {'─' * 48}")
    print(f"  Regular member  : {name1}, Age {age1}, BMI {bmi1:.2f}")
    print(f"  Premium member  : {name2}, Age {age2}, BMI {bmi2:.2f}")
    print(f"  Trainer         : {trainer}")
    print(f"  Monthly fee     : ${fee:.2f}  |  Yearly : ${total_yearly:.2f}")
    print(f"  Sessions/week   : {sessions}  |  Cost/session : ${cost_per_session:.2f}")
    print(f"  Weekly calories : ~{weekly_calories} kcal burned")
    print(f"  {'─' * 48}")
    print(f"  {name1} is {'active' if is_active1 else 'inactive'}.")
    print(f"  {name2} is {'active' if is_active2 else 'inactive'} with trainer {trainer}.")
    print(f"  {'=' * 48}")
    print(f"\n  Program completed successfully. No errors.\n")


# Entry point
if __name__ == "__main__":
    main()
