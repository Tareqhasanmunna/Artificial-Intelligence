import heapq

def greedy(graph, start, goal, heuristic):
    # Create a priority queue and push the start node with its heuristic value
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], start))
    visited = set()

    while priority_queue:
        # Pop the node with the smallest heuristic value
        cost = heapq.heappop(priority_queue)
        current = cost[1]

        # Skip if the current node has already been visited
        if current in visited:
            continue
        visited.add(current)

        print(f"Visited: {current}")

        # If the goal is reached, print and return
        if current == goal:
            print("Goal reached")
            return

        # Add neighbors to the priority queue with their heuristic values
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))

# Example graph and heuristic values
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 2,
    'E': 1,
    'F': 0
}

# Run the greedy search
greedy(graph, 'A', 'F', heuristic)
