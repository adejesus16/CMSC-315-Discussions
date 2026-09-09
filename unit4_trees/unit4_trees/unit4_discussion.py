"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value  # Key/Data value stored in the node
        self.left = None    # Pointer/reference to left child node (smaller values)
        self.right = None   # Pointer/reference to right child node (larger values)


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None  # Tree starts empty with root pointing to None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # Insertion relies on BST invariant: values strictly smaller than the node
        # must go to the left, and values strictly larger must go to the right.
        # This preserves ordering so future logarithmic searches stay valid.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # Base case: If leaf position reached, instantiate new Node
        if node is None:
            return Node(value)

        # Recursion step: traverse left if smaller, right if larger
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        else:
            # Duplicate values: Here we ignore duplicates to avoid redundant nodes
            pass

        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # BST search is O(log n) on average because at each comparison step,
        # half of the remaining subtrees are eliminated from consideration,
        # unlike linear search which must inspect elements sequentially O(n).
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # Base cases: value not found (None) or match found
        if node is None:
            return False
        if node.value == value:
            return True

        # Recursive search based on ordering property
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node:
            # 1. Traverses all smaller elements first in left subtree
            self._inorder_recursive(node.left, values)
            # 2. Visits current parent element
            values.append(node.value)
            # 3. Traverses all larger elements in right subtree
            # This order guarantees output in strictly ascending sequence.
            self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    print("\n=== TREE CONSTRUCTION ===")
    bst = BST()
    # Inserting 7 values in balanced order so both left and right subtrees exist
    values_to_insert = [50, 30, 70, 20, 40, 60, 80]

    # BST search space reduction:
    # Starting with root key 50, every search branch decision reduces search scope by ~50%,
    # achieving O(log n) lookups when tree structure remains relatively balanced.
    print(f"Inserting values into BST: {values_to_insert}")
    for v in values_to_insert:
        bst.insert(v)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    print("\n=== IN-ORDER TRAVERSAL ===")
    traversal_result = bst.inorder()
    print(f"In-Order Traversal Result: {traversal_result}")
    # In-order traversal visits (Left, Root, Right), which guarantees
    # printed values are in ascending numerical order.

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    print("\n=== SEARCH TESTS ===")
    # Existing values test
    existing_tests = [30, 80]
    for val in existing_tests:
        found = bst.search(val)
        print(f"Search for {val} (Expected True): {found}")

    # Non-existing values test
    missing_tests = [15, 95]
    for val in missing_tests:
        found = bst.search(val)
        print(f"Search for {val} (Expected False): {found}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    print("\n=== EDGE CASES ===")
    # Edge Case 1: Searching and traversing an empty tree
    empty_bst = BST()
    print(f"Empty Tree Traversal: {empty_bst.inorder()}")
    print(f"Search on Empty Tree (10): {empty_bst.search(10)}")

    # Edge Case 2: Attempting duplicate insertion
    bst.insert(50)  # Duplicate root value
    print(f"Traversal after duplicate 50 insert attempt: {bst.inorder()}")


if __name__ == "__main__":
    main()