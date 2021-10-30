from itertools import combinations

N, M = map(int, input().split())
graph = []
possible = [] # All possible corrinates to place walls
virus = [] # Coorinates of all viruses
for i in range(N):
  graph.append(list(map(int, input().split())))
  for j in range(M):
    if graph[i][j] == 0:
      possible.append([i, j])
    if graph[i][j] == 2:
      virus.append([i, j])

walls = list(combinations(possible, 3))
