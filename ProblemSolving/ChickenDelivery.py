from itertools import combinations
N, M = map(int, input().split())

houses = []
chickens = []

for r in range(N):
  info = list(map(int, input().split()))
  for c in range(N):
    if info[c] == 1:
      houses.append((r + 1, c +1))
    if info[c] == 2:
      chickens.append((r + 1, c +1))
print(chickens)
combination = list(combinations(chickens, M))

result = 999999
for combo in combination:
  combo_dist = 0
  for house in houses:
    chicken_dist = 9999999
    for chicken in combo:
      distance = abs(chicken[0] - house[0]) + abs(chicken[1] - house[1])
      if distance < chicken_dist:
        chicken_dist = distance
    combo_dist += chicken_dist
    print(combo_dist)
  if result < combo_dist:
    result = combo_dist

print(result)

"""
chicken_distance = 0
for house in houses:
  shortest = 999999
  for chicken in chickens:
    distance = abs(chicken[0] - house[0]) + abs(chicken[1] - house[1])
    if distance < shortest:
      shortest = distance
  chicken_distance += shortest

"""