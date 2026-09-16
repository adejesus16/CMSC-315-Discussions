"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.
"""

def linear_search(lst, target):
    """
    Implements a linear search algorithm.
    - Searches the list from beginning to end.
    - Returns the index if the target is found.
    - Returns -1 if the target is not found.

    Time Complexity: O(n) because in the worst-case scenario,
    every element in the list must be checked individually.
    """
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


def binary_search(lst, target):
    """
    Implements a binary search algorithm.
    - Assumes the list is already sorted.
    - Repeatedly reduces the search space by half.
    - Returns the index if the target is found.
    - Returns -1 if the target is not found.

    Time Complexity: O(log n) because each iteration cuts
    the remaining search range in half.
    """
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            # Discard left half
            left = mid + 1
        else:
            # Discard right half
            right = mid - 1

    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # SMALL DATASET TEST
    # ===============================
    print("\n=== SMALL DATASET TEST ===")
    small_list = [3, 11, 25, 38, 42, 50]

    # Test existing value (42)
    target_exist = 42
    print(f"Searching for {target_exist} in {small_list}:")
    print(f"Linear Search Index: {linear_search(small_list, target_exist)}")
    print(f"Binary Search Index: {binary_search(small_list, target_exist)}")

    # Test non-existing value (20)
    target_missing = 20
    print(f"Searching for {target_missing} in {small_list}:")
    print(f"Linear Search Index: {linear_search(small_list, target_missing)}")
    print(f"Binary Search Index: {binary_search(small_list, target_missing)}")


    # ===============================
    # LARGE DATASET TEST
    # ===============================
    print("\n=== LARGE DATASET TEST ===")
    # Create a sorted list of 10,000 integers
    large_list = list(range(0, 20000, 2))
    large_target = 15488

    print(f"Searching for {large_target} in a large dataset of {len(large_list)} elements.")
    print(f"Linear Search Index: {linear_search(large_list, large_target)}")
    print(f"Binary Search Index: {binary_search(large_list, large_target)}")
    # Binary search is significantly faster on large datasets because
    # it eliminates half of the remaining elements with each step,
    # whereas linear search must check elements sequentially.


    # ===============================
    # EDGE CASE TESTS
    # ===============================
    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1: Empty list
    empty_list = []
    print(f"Empty list search result: {binary_search(empty_list, 5)}")
    # Explanation: Returns -1 immediately because the search boundaries are invalid (left > right).

    # Edge Case 2: Single-element list (Target present)
    single_list = [42]
    print(f"Single-element list (found) result: {binary_search(single_list, 42)}")
    # Explanation: left, right, and mid are all 0, matching the target immediately.

    # Edge Case 3: Target at the first position
    print(f"Target at first position result: {binary_search(small_list, 3)}")
    # Explanation: Binary search handles boundaries correctly when the target matches the initial mid or moves left.


if __name__ == "__main__":
    main()