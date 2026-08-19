"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class Patient:
    facility_name = "Community Health Center"

    def __init__(self, name, patient_id):
        self.name = name
        self.patient_id = patient_id

    def display_info(self):
        return f"Patient Name: {self.name}, Patient ID: {self.patient_id}"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class Inpatient(Patient):
    patient_type = "Inpatient"

    def __init__(self, name, patient_id, room_number, days_admitted):
        super().__init__(name, patient_id)
        self.room_number = room_number
        self.days_admitted = days_admitted

    def calculate_stay(self):
        return f"{self.name} has been admitted for {self.days_admitted} days."

    def calculate_cost(self, daily_rate):
        if daily_rate < 0:
            return "Invalid daily rate. Rate cannot be negative."
        return self.days_admitted * daily_rate

    def display_info(self):
        return (f"Patient Name: {self.name}, Patient ID: {self.patient_id}, "
                f"Room Number: {self.room_number}, Days Admitted: {self.days_admitted}")


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    patient1 = Inpatient("Maria", 101, 201, 3)
    patient2 = Inpatient("James", 102, 202, 5)

    # Access the class variable through the class.
    print("Class variable through class:", Inpatient.patient_type)

    # Access the same class variable through an object.
    print("Class variable through object:", patient1.patient_type)

    # Add a new attribute to only one object.
    patient1.insurance_provider = "HealthCare Plus"

    # Display each object's namespace.
    print("Patient 1 namespace:", patient1.__dict__)
    print("Patient 2 namespace:", patient2.__dict__)

    # Display information about the class namespace.
    print("Inpatient class namespace:", Inpatient.__dict__)


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    patient_record = {
        "name": "Maria",
        "medications": ["Medication A", "Medication B"]
    }

    shallow_record = copy(patient_record)
    deep_record = deepcopy(patient_record)

    # Change the original nested list.
    patient_record["medications"].append("Medication C")

    # A shallow copy shares the same nested list with the original.
    # A deep copy creates a separate copy of the nested data.
    print("Original record:", patient_record)
    print("Shallow copy:", shallow_record)
    print("Deep copy:", deep_record)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n=== Parent Object ===")
    patient = Patient("Alex Johnson", 1001)
    print(patient.display_info())
    print("Facility:", patient.facility_name)

    print("\n=== Child Object ===")
    inpatient = Inpatient("Taylor Smith", 1002, 305, 4)
    print(inpatient.display_info())
    print(inpatient.calculate_stay())
    print("Estimated Stay Cost: $", inpatient.calculate_cost(250))
    # Test an edge case with an invalid negative daily rate.
    print("Invalid Cost Test:", inpatient.calculate_cost(-100))
    print("Patient Type:", inpatient.patient_type)

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()