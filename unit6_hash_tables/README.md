# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.

## Completed Implementation

I created a course tracker using a Python dictionary to demonstrate how a hash table works. The course codes were used as unique keys, and the course names were stored as their values.

I demonstrated the main hash table operations by inserting five courses, looking up courses by their keys, updating an existing value, and deleting a key-value pair. I also tested missing keys to show how the program could handle situations where a requested key was not stored in the dictionary.

Python dictionaries use hashing to help locate values based on their keys. This makes dictionaries useful when information needs to be retrieved quickly. A course tracker was a real-world example because a course code could be used as a unique identifier to locate the information associated with that course.