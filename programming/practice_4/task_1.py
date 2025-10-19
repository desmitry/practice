class Employee:
    """Represents a general employee."""

    def __init__(self, name, base_salary):
        """Initializes the employee."""
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        """Calculates the salary for an employee."""
        return self.base_salary


class Manager(Employee):
    """Represents a manager."""

    def __init__(self, name, base_salary, bonus):
        """Initializes the manager."""
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        """Calculates the salary for a manager."""
        return self.base_salary + self.bonus


class Developer(Employee):
    """Represents a developer."""

    def __init__(self, name, base_salary, hourly_rate, hours_worked):
        """Initializes the developer."""
        super().__init__(name, base_salary)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        """Calculates the salary for a developer."""
        return self.base_salary + (self.hourly_rate * self.hours_worked)
