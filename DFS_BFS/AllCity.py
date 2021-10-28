from collections import deque

N, M, K, start = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
  A, B = map(int, input().split())
  graph[A].append(B)

distance = [-1] * (N + 1)
queue = deque([start])
distance[start] = 0

while queue:
  q = queue.popleft()
  for city in graph[q]:
    if distance[city] == -1:
      queue.append(city)
      distance[city] = distance[q] + 1

none = False
for i in range(1, N + 1):
  if distance[i] == K:
    print(i)
    none = True

if not none:
  print(-1)
