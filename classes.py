# ============================================================
#  classes.py
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


# ------------------------------------------------------------
#  PART 2 - Inheritance
#  PART 3 - Magic Methods (dunder methods)
#  PART 4 - Decorators (@staticmethod, @classmethod, @property)
# ------------------------------------------------------------


class Member:
    """
    PARENT CLASS - represents a standard gym member.

    Part 3 - Magic methods implemented:
        __str__  : controls what print(member) displays
        __eq__   : compares two members by name
        __len__  : returns the member's age

    Part 4 - Decorators implemented:
        @staticmethod  -> calculate_bmi(weight, height)
        @classmethod   -> get_total_members()
    """

    # Class variable - shared across ALL instances
    total_members = 0

    def __init__(self, name: str, age: int, weight: float,
                 height: float, is_active: bool):
        """
        Constructor - initializes a regular gym member.

        Parameters:
            name      (str)   : full name of the member
            age       (int)   : age in years
            weight    (float) : weight in kilograms
            height    (float) : height in metres
            is_active (bool)  : True if membership is active
        """
        self.name      = name
        self.age       = age
        self.weight    = weight      # kg
        self.height    = height      # metres
        self.is_active = is_active

        # Increment the class-level counter each time a member is created
        Member.total_members += 1

    # --------------------------------------------------------
    #  PART 3 - Magic Methods
    # --------------------------------------------------------

    def __str__(self) -> str:
        """
        Magic method __str__
        Controls what is displayed when you do: print(member)
        Instead of <__main__.Member object at 0x...>, it shows
        a clean readable summary.
        """
        status = "Active" if self.is_active else "Inactive"
        bmi = Member.calculate_bmi(self.weight, self.height)
        return (f"[Member] {self.name} | Age: {self.age} | "
                f"BMI: {bmi:.2f} | Status: {status}")

    def __eq__(self, other) -> bool:
        """
        Magic method __eq__
        Defines what == means for two Member objects.
        Two members are considered equal if they have the same name
        (case-insensitive comparison).

        Example: member1 == member2  ->  True or False
        """
        if isinstance(other, Member):
            return self.name.lower() == other.name.lower()
        return False

    def __len__(self) -> int:
        """
        Magic method __len__
        Defines what len() returns for a Member object.
        For a regular member, len(member) returns the member's age.

        Example: len(member1)  ->  25
        """
        return self.age

    # --------------------------------------------------------
    #  PART 4 - Decorators
    # --------------------------------------------------------

    @staticmethod
    def calculate_bmi(weight: float, height: float) -> float:
        """
        Decorator @staticmethod
        A static method belongs to the CLASS, not to any instance.
        It does NOT receive 'self' or 'cls' as first argument.
        It can be called without creating an object.

        Usage: Member.calculate_bmi(70.0, 1.75)
               member1.calculate_bmi(70.0, 1.75)

        Formula: BMI = weight (kg) / height (m) squared
        """
        return weight / (height ** 2)

    @classmethod
    def get_total_members(cls) -> int:
        """
        Decorator @classmethod
        A class method receives the CLASS itself as the first argument (cls).
        Used to access or modify class-level data.
        Here it reads the total_members counter.

        Usage: Member.get_total_members()
        """
        return cls.total_members

    # --------------------------------------------------------
    #  Display method
    # --------------------------------------------------------

    def display_info(self) -> None:
        """Prints a formatted info card for the member."""
        bmi    = Member.calculate_bmi(self.weight, self.height)
        status = "Active" if self.is_active else "Inactive"

        print(f"\n{'─' * 46}")
        print(f"  Name    : {self.name}")
        print(f"  Age     : {self.age} years")
        print(f"  Weight  : {self.weight:.1f} kg")
        print(f"  Height  : {self.height:.2f} m")
        print(f"  BMI     : {bmi:.2f}")
        print(f"  Status  : {status}")
        print(f"{'─' * 46}")


# ============================================================

class PremiumMember(Member):
    """
    CHILD CLASS - PremiumMember IS A Member with extra benefits.

    Part 2 - Inheritance:
        - Inherits all attributes and methods from Member
        - Calls super().__init__() to reuse the parent constructor
        - Adds 3 new attributes: trainer_name, monthly_fee, sessions_per_week
        - Adds new method: display_premium_info()

    Part 3 - Magic methods overridden:
        __str__  : extended version showing premium details
        __len__  : returns sessions per week instead of age

    Part 4 - Decorator added:
        @property  -> yearly_cost
    """

    def __init__(self, name: str, age: int, weight: float,
                 height: float, is_active: bool,
                 trainer_name: str, monthly_fee: float,
                 sessions_per_week: int):
        """
        Constructor - initializes a premium gym member.
        Calls the parent constructor first using super().__init__()
        then adds premium-specific attributes.

        Extra parameters:
            trainer_name      (str)   : assigned personal trainer
            monthly_fee       (float) : monthly subscription cost in USD
            sessions_per_week (int)   : number of training sessions per week
        """
        # -- PART 2: Call the parent constructor --
        # This sets: name, age, weight, height, is_active
        # and increments Member.total_members
        super().__init__(name, age, weight, height, is_active)

        # -- New attributes specific to PremiumMember --
        self.trainer_name      = trainer_name
        self.monthly_fee       = monthly_fee        # float - USD per month
        self.sessions_per_week = sessions_per_week  # int   - times per week

    # --------------------------------------------------------
    #  PART 4 - @property Decorator
    # --------------------------------------------------------

    @property
    def yearly_cost(self) -> float:
        """
        Decorator @property
        Transforms a method into an attribute-style access.
        No parentheses needed when calling it.

        Usage:  premium.yearly_cost       (NOT premium.yearly_cost())
        Returns: monthly_fee * 12
        """
        return self.monthly_fee * 12

    # --------------------------------------------------------
    #  PART 3 - Magic Methods (overridden from parent)
    # --------------------------------------------------------

    def __str__(self) -> str:
        """
        Overrides the parent __str__.
        Reuses the parent version with super().__str__()
        and adds premium-specific information.
        """
        base = super().__str__().replace("[Member]", "[Premium]")
        return (f"{base}\n"
                f"          Trainer: {self.trainer_name} | "
                f"Fee: ${self.monthly_fee:.2f}/mo | "
                f"Sessions: {self.sessions_per_week}x/week")

    def __len__(self) -> int:
        """
        Overrides the parent __len__.
        For a PremiumMember, len() returns sessions per week
        instead of age.

        Example: len(premium1)  ->  4
        """
        return self.sessions_per_week

    # --------------------------------------------------------
    #  Display method
    # --------------------------------------------------------

    def display_premium_info(self) -> None:
        """
        Prints a full formatted info card for the premium member.
        Calls the parent display_info() first, then adds premium details.
        Includes 3 arithmetic expressions (Part 1).
        """
        # Call the parent display method
        self.display_info()

        # -- PART 1: Arithmetic expressions --
        yearly           = self.yearly_cost                           # expression 1: monthly * 12
        weekly_calories  = 450 * self.sessions_per_week               # expression 2: calories per session * sessions
        cost_per_session = (self.monthly_fee / (self.sessions_per_week * 4)
                            if self.sessions_per_week > 0 else 0)     # expression 3: fee / total sessions per month

        print(f"  Trainer         : {self.trainer_name}")
        print(f"  Monthly Fee     : ${self.monthly_fee:.2f}")
        print(f"  Yearly Cost     : ${yearly:.2f}")
        print(f"  Cost/Session    : ${cost_per_session:.2f}")
        print(f"  Sessions/Week   : {self.sessions_per_week}")
        print(f"  Est. Weekly Cal : {weekly_calories} kcal burned")
        print(f"{'─' * 46}\n")