from collections import deque 

graph = {
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

# dfs using stack
def bfs_stack(graph, start_node):
  visited = list()
  q = deque()

  q.append(start_node)

  while q:
    now = q.popleft()
    if now not in visited:
      visited.append(now)
      q.extend(graph[now])

  return visited

print(bfs_stack(graph, 'A'))