# Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u v, vertex u comes before v in the ordering. Topological Sorting for a graph is not possible if the graph is not a DAG.

# Indegree =  number of edge pointing towards this node

# O(V + E)

from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v + 1)
graph = [[] for i in range(v + 1)]

for _ in range(e):
   a, b = map(int, input().split())
   graph[a].append(b) # a -> b
   indegree[b] += 1

def topological_sort():
  result = []
  q = deque() # using Queue

  for i in range(1, v + 1):
    if indegree[i] == 0:
      q.append(i)
    
  while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append(i)

  for i in result:
    print(i, end = ' ')

topological_sort()