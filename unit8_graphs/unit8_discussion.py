"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """

    # If the starting node is not in the graph, return an empty list.
    if start not in graph:
        return []

    # A set keeps track of nodes that have already been visited.
    # This prevents the same node from being processed more than once.
    visited = set()

    # A queue is used because BFS follows First-In, First-Out (FIFO) order.
    # This allows BFS to visit nodes level by level.
    queue = deque([start])

    # This list stores the order in which the nodes are visited.
    traversal_order = []

    # Continue searching while there are nodes waiting in the queue.
    while queue:
        # Remove the node that has been waiting the longest.
        current = queue.popleft()

        # Only process the node if it has not already been visited.
        if current not in visited:
            visited.add(current)
            traversal_order.append(current)

            # Add each unvisited neighbor to the queue so it can
            # be explored after the current level is processed.
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)

    # BFS uses a queue and explores nearby nodes first.
    # DFS is different because it goes deeper along one path before
    # returning to explore other paths.

    return traversal_order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    print("\n=== GRAPH STRUCTURE ===")
    # This graph represents buildings on a college campus.
    # Each building is a node, and each connection represents
    # a walking path between two buildings.
    graph = {
        "Library": ["Science Hall", "Student Center"],
        "Science Hall": ["Library", "Gym"],
        "Student Center": ["Library", "Cafeteria"],
        "Gym": ["Science Hall", "Cafeteria"],
        "Cafeteria": ["Student Center", "Gym", "Dorm"],
        "Dorm": ["Cafeteria"]
    }

    # Display each building and the buildings directly connected to it.
    for building, neighbors in graph.items():
        print(f"{building}: {neighbors}")

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")
    # Start the BFS traversal at the Library.
    start_node = "Library"

    # BFS visits the starting node first and then explores
    # all neighboring nodes level by level.
    traversal = bfs(graph, start_node)

    print(f"Starting node: {start_node}")
    print(f"BFS traversal order: {traversal}")

    # Add a new building to the graph and connect it to the Dorm.
    # This demonstrates how adding a node changes the traversal.
    graph["Computer Lab"] = ["Dorm"]
    graph["Dorm"].append("Computer Lab")

    print("\nAdded Computer Lab connected to Dorm.")

    # Run BFS again to show the updated traversal.
    updated_traversal = bfs(graph, start_node)
    print(f"Updated BFS traversal: {updated_traversal}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    # Edge Case 1: Try to start BFS from a building that does not exist.
    # The bfs function safely returns an empty list because the
    # starting node is not found in the graph.
    missing_start = "Parking Garage"
    missing_result = bfs(graph, missing_start)

    print("\nEdge Case 1: Missing starting node")
    print(f"Starting node: {missing_start}")
    print(f"Traversal result: {missing_result}")
    print("Explanation: The starting node does not exist, so BFS returns an empty list.")

    # Edge Case 2: Test a graph containing only one node.
    # Since the node has no neighbors, BFS visits that node and then stops.
    single_node_graph = {
        "Bookstore": []
    }

    single_result = bfs(single_node_graph, "Bookstore")

    print("\nEdge Case 2: Graph with one node")
    print("Starting node: Bookstore")
    print(f"Traversal result: {single_result}")
    print("Explanation: BFS visits Bookstore and stops because it has no neighbors.")



if __name__ == "__main__":
    main()
