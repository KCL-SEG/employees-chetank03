"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee:  # main class
    def __init__(self, name, commission_type="", commission=0, num_contracts=0):
        self.name = name  # name of the employee.
        self.commission_type = (
            commission_type  # type of commission the employee recieves.
        )
        self.num_contracts = (
            num_contracts  # num of contract if commission type is contract.
        )
        self.commission = commission  # amount of commission.


class MonthlyEmployee(Employee):  # sub class of employee who get payed monthly.
    def __init__(self, name, salary, commission_type="", commission=0, num_contracts=0):
        super().__init__(name, commission_type, commission, num_contracts)

        self.salary = salary

    def get_pay(self):  # calculates the total pay with commission(if recieved).
        if self.commission_type == ("bonus"):
            return self.salary + self.commission

        elif self.commission_type == ("contract"):
            return self.salary + (self.commission * self.num_contracts)

        else:
            return self.salary

    def __str__(self):
        if self.commission_type == ("bonus"):
            return f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.commission}.  Their total pay is {self.get_pay()}."

        elif self.commission_type == ("contract"):
            return f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.num_contracts} contract(s) at {self.commission}/contract.  Their total pay is {self.get_pay()}."

        else:
            return f"{self.name} works on a monthly salary of {self.salary}.  Their total pay is {self.get_pay()}."


class ContractEmployee(
    Employee
):  # sub class of employee who get payed on a contract hourly.
    def __init__(
        self,
        name,
        hourly_pay,
        num_hours,
        commission_type="",
        commission=0,
        num_contracts=0,
    ):
        super().__init__(name, commission_type, commission, num_contracts)

        self.hourly_pay = hourly_pay
        self.num_hours = num_hours

        self.total_salary = hourly_pay * num_hours

    def get_pay(self):  # calculates the total pay with commission(if recieved).
        if self.commission_type == ("bonus"):
            return self.total_salary + self.commission

        elif self.commission_type == ("contract"):
            return self.total_salary + (self.commission * self.num_contracts)

        else:
            return self.total_salary

    def __str__(self):
        if self.commission_type == ("bonus"):
            return f"{self.name} works on a contract of {self.num_hours} hours at {self.hourly_pay}/hour and receives a bonus commission of {self.commission}.  Their total pay is {self.get_pay()}."

        elif self.commission_type == ("contract"):
            return f"{self.name} works on a contract of {self.num_hours} hours at {self.hourly_pay}/hour and receives a commission for {self.num_contracts} contract(s) at {self.commission}/contract.  Their total pay is {self.get_pay()}."

        else:
            return f"{self.name} works on a contract of {self.num_hours} hours at {self.hourly_pay}/hour.  Their total pay is {self.get_pay()}."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = MonthlyEmployee("Billie", 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = ContractEmployee("Charlie", 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = MonthlyEmployee("Renee", 3000, "contract", 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = ContractEmployee("Jan", 25, 150, "contract", 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = MonthlyEmployee("Robbie", 2000, "bonus", 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = ContractEmployee("Ariel", 30, 120, "bonus", 600)
