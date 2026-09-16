# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
   While completing this assignment, I reinforced my practical understanding of linear and binary search algorithms and how to analyze their time complexities ($O(n)$ vs $O(\log n)$).

2. What challenges did you encounter, and how did you overcome them?
   A primary challenge was correctly handling index boundaries in binary search to prevent infinite loops, which I overcame by carefully managing the `left`, `right`, and `mid` pointer updates.

3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.
   inear search is ideal for small or unsorted datasets where sorting overhead is unnecessary. Binary search is significantly more efficient for large-scale, high-frequency lookups because it cuts the search space in half with every iteration, provided that the data is pre-sorted.