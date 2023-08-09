class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
    
    def get_name(self):
        return self._name

    def get_salary(self):
        return self._salary

    def print_details(self):
        print("Employee Name:", employee.get_name())
        print("Employee Salary:", employee.get_salary())

    def get_salary(self):
        return self._salary

    def pay_increment(self, increment_amount):
        if increment_amount > 0:
            self._salary += increment_amount
        else:
            raise ValueError("Increment amount must be a positive number.")

# Creating an instance of the Employee class
employee = Employee("Simon Peter", 5000000)

# Display initial information
employee.print_details()

# Giving a pay increment of 1000
employee.pay_increment(500000)

# Display new information
employee.print_details()
