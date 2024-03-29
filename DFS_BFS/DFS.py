# Depth-First Search

graph_recursive = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

visited = [False] * 9

graph_stack = {
  'A': ['B'],
  'B': ['A', 'C', 'H'],
  'C': ['B', 'D'],
  'D': ['C', 'E', 'G'],
  'E': ['D', 'F'],
  'F': ['E'],
  'G': ['D'],
  'H': ['B', 'I', 'J', 'M'],
  'I': ['H'],
  'J': ['H', 'K'],
  'K': ['J', 'L'],
  'L': ['K'],
  'M': ['H']
}

# recursive O(N)
def dfs_recursive(graph, v, visited):
  visited[v] = True
  print(v, end = ' ')
  for i in graph[v]:
    if not visited[i]:
      dfs_recursive(graph, i, visited)

#dfs_recursive(graph_recursive, 1, visited)


# dfs using stack
def dfs_stack(graph, start_node):
  visited = list()
  stack = list()

  stack.append(start_node)

  while stack:
    now = stack.pop()
    if now not in visited:
      visited.append(now)
      stack.extend(reversed(graph[now]))

  return visited

print(dfs_stack(graph_stack, 'A'))



