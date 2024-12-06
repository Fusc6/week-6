# Implementing the classes based on the provided diagram and instructions

class Person:
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

    def print_person_details(self):
        return f"Name: {self.first_name} {self.last_name}\nDate of Birth: {self.date_of_birth}"


class Worker:
    def __init__(self, tax_file_number, super_number):
        self.tax_file_number = tax_file_number
        self.super_number = super_number

    def get_info(self):
        return f"Tax File Number: {self.tax_file_number}\nSuper Number: {self.super_number}"


class Employee2(Person, Worker):
    def __init__(self, first_name, last_name, date_of_birth, tax_file_number, super_number, employ_id, position):
        # Initializing attributes from both base classes
        Person.__init__(self, first_name, last_name, date_of_birth)
        Worker.__init__(self, tax_file_number, super_number)
        self.employ_id = employ_id
        self.position = position

    def get_details(self):
        person_details = self.print_person_details()
        worker_info = self.get_info()
        return (
            f"{person_details}\n"
            f"{worker_info}\n"
            f"Employee ID: {self.employ_id}\nPosition: {self.position}"
        )


#test
kim = Employee2("Kim", "White", "12/08/2020", 4556655, 567, 1121, "Developer")
kim_details = kim.get_details()
kim_details
