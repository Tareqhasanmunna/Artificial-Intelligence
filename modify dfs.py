def dfs(graph,start_node):
  stack=[start_node]
  visited= set()
  traversal_order= []

  while stack:
    current_node = stack.pop()
    if current_node not in visited:
      visited.add(current_node)
      traversal_order.append(current_node)

      for neighbor in reversed(graph[current_node]):
        stack.append(neighbor)
    if len(visited) == len(graph):

        return 'Graph is connected', traversal_order
  else:
        return 'Graph is not connected', traversal_order
  
def count_nodes(graph):
  counted = 0
  all_visited =[]
  for node in graph:
    if node not in all_visited:
      visited = dfs(graph, node)
      all_visited.extend(visited)
      counted += 1
  return counted

graph = {
      '5': ['3','7'],
      '3': ['2','4'],
      '7': ['8'],
      '2': [],
      '4': ['8'],
      '8': []
  }

start_node = '5'
print('DFS traversal',dfs(graph,start_node),'Connected Component: ',count_nodes(graph))