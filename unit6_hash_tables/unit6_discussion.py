"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.
    # Create an empty dictionary to store course information.
    # Python dictionaries behave like hash tables by using
    # unique keys to quickly store and retrieve values.
    courses = {}

    # Add five course codes and course names to the dictionary.
    courses["CMSC 315"] = "Data Structures and Algorithms"
    courses["CMSC 320"] = "Relational Database"
    courses["CMSC 330"] = "Advanced Programming Languages"
    courses["CMSC 335"] = "Object-Oriented and Concurrent Programming"
    courses["CMSC 495"] = "Current Trends and Projects in Computer Science"

    print("\n=== INSERT OPERATIONS ===")
    print("Courses in the hash table:")
    print(courses)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    # Look up two courses by using their unique course codes as keys.
    # A dictionary uses the key to efficiently locate its associated value.
    course_one = courses["CMSC 315"]
    course_two = courses["CMSC 320"]

    # Display the results of both successful lookups.
    print("CMSC 315:", course_one)
    print("CMSC 320:", course_two)

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.


    print("\n=== UPDATE OPERATIONS ===")
    # Display the dictionary before changing an existing value.
    print("Before update:")
    print(courses)

    # Assigning a new value to an existing key updates that key's value
    # instead of creating another copy of the key.
    courses["CMSC 320"] = "Database Systems"

    # Display the dictionary after the update.
    print("After update:")
    print(courses)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    # Display the dictionary before removing a course.
    print("Before deletion:")
    print(courses)

    # Delete CMSC 495 from the dictionary.
    # Removing the key also removes its associated value.
    del courses["CMSC 495"]

    # Display the dictionary after the course has been removed.
    print("After deletion:")
    print(courses)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    # Edge Case 1: Try to look up a course that is not in the dictionary.
    # Using get() prevents an error and returns the provided default message.
    missing_course = courses.get("CMSC 999", "Course not found.")
    print("Missing course lookup:", missing_course)

    # Edge Case 2: Safely try to delete a course that does not exist.
    # Check for the key first so the program does not cause a KeyError.
    if "CMSC 999" in courses:
        del courses["CMSC 999"]
        print("CMSC 999 was removed.")
    else:
        print("CMSC 999 cannot be deleted because it is not in the dictionary.")



if __name__ == "__main__":
    main()