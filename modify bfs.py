from collections import deque

def bfs(graph, start, obstacles):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        node = queue.popleft()        
        for neighbor in graph[node]:
            if neighbor not in visited and neighbor not in obstacles:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

obstacles = {'D'}
print(bfs(graph, 'A', obstacles))