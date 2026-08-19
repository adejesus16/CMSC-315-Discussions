# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.

## Implementation Documentation

For this assignment, I created a healthcare system that demonstrated object-oriented programming concepts in Python. I created a Patient parent class that stored basic patient information, including the patient's name and ID. I also used a class variable to store the name of the healthcare facility.I created an Inpatient child class that inherited from the Patient class. The Inpatient class added a room number and the number of days the patient was admitted. I also added methods to display inpatient information, calculate the length of the patient's stay, and estimate the cost of the stay.I demonstrated class and instance namespaces by creating multiple Inpatient objects and adding an insurance provider attribute to only one object. I used __dict__ to examine the differences between the objects and the class.I also demonstrated shallow and deep copying using a patient record containing a nested medication list. After modifying the original list, the shallow copy reflected the change while the deep copy remained unchanged.As my student-created extension, I added a method that calculated the estimated cost of an inpatient stay using the number of days admitted and a daily rate.I also tested an edge case by providing a negative daily rate. The program handled the invalid value by displaying an error message instead of calculating an incorrect negative cost.