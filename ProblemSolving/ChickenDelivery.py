from itertools import combinations
N, M = map(int, input().split())
INF = int(1e9)

houses = []
chickens = []

for r in range(N):
  info = list(map(int, input().split()))
  for c in range(N):
    if info[c] == 1:
      houses.append((r, c))
    if info[c] == 2:
      chickens.append((r, c))

combination = list(combinations(chickens, M))

result = INF
for combo in combination:
  total_distance = 0
  for house in houses:
    shortest_chicken = INF
    for chicken in combo:
      distance = abs(chicken[0] - house[0]) + abs(chicken[1] - house[1])
      shortest_chicken = min(shortest_chicken, distance)
    total_distance += shortest_chicken
  result = min(result, total_distance)

print(result)