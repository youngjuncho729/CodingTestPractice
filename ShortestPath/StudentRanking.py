n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1

for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      if graph[a][b] == 0:
        graph[a][b] = 1 if graph[a][k] + graph[k][b] >= 2 else 0
print(graph)

result = [0] * (n + 1)
for i in range(1, n + 1):
  for j in range(1, n + 1):
    result[i] += graph[i][j]
    result[j] += graph[i][j]

for i in range(1, n + 1):
  if result[i] == n - 1:
    print(i)