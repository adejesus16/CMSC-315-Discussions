# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

---

## Implementation & Documentation Details

### Code Implementation Summary
- Constructed a `Node` class storing values along with left/right child references.
- Implemented a `BST` class featuring recursive private helpers (`_insert_recursive`, `_search_recursive`, and `_inorder_recursive`)[cite: 2].
- Constructed a test binary search tree inserting values `[50, 30, 70, 20, 40, 60, 80]`, establishing populated left and right subtrees[cite: 2].
- Verified in-order traversal results to confirm elements were sorted in ascending order (`[20, 30, 40, 50, 60, 70, 80]`)[cite: 2].
- Tested search queries for existing keys (`30`, `80`) and missing keys (`15`, `95`)[cite: 2].
- Handled edge cases including querying empty trees without raising exceptions and preventing duplicate key insertions[cite: 2].

### Discussion Board Reflection Answers

1. **What concepts or skills did you learn while completing this assignment?**
   I strengthened my understanding of recursive tree traversal, pointer manipulation, and conditional branching in node-based data structures. I learned how recursive helper methods allow clean subtree navigation and how in-order traversal (Left -> Root -> Right) systematically yields sorted outputs.

2. **What challenges did you encounter, and how did you overcome them?**
   My primary challenge was managing node pointer assignment during recursive insertion steps. Initially, subtree references were not updating correctly. I resolved this by ensuring `_insert_recursive` always returned the updated node pointer (`return node`) so parent nodes correctly reassigned child references

3. **Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.**
   A Binary Search Tree relies on a strict ordering rule where left descendants are smaller than parent keys, while right descendants are larger. In comparison to linear data structures (like unsorted arrays or linked lists) that demand O(n) time complexity, a balanced BST continuously halves the remaining search scope during each step, resulting in O(log n) average search efficiency.