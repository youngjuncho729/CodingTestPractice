from collections import deque
import copy

n = int(input())
graph = [[] for i in range(n + 1)]
indegree = [0] * (n + 1)
time = [0] * (n + 1)

for i in range(1, n + 1):
  data = list(map(int, input().split()))
  time[i] = data[0]
  for x in data[1:-1]:
    indegree[i] += 1
    graph[x].append(i)

def topology():
  result = copy.deepcopy(time)
  q = deque()
  
  for i in range(1, n + 1):
    if indegree[i] == 0:
      q.append(i)
  
  while q:
    now = q.popleft()
    for x in graph[now]:
      result[x] = max(result[x], result[now] + time[x])
      indegree[x] -= 1
      if indegree[x] == 0:
        q.append(x)
  
  for i in range(1, n + 1):
    print(result[i])

topology()