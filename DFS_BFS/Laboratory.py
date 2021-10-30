import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
temp = [[0] * M for _ in range(N)] 
possible = [] # All possible corrinates to place walls
viruses = [] # Coordinates of all viruses
for i in range(N):
  graph.append(list(map(int, input().split())))
  for j in range(M):
    if graph[i][j] == 0:
      possible.append([i, j])
    if graph[i][j] == 1:
      temp[i][j] = 1
    if graph[i][j] == 2:
      viruses.append([i, j])
      temp[i][j] = 2

new_walls = list(combinations(possible, 3))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def spread(x, y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= 0 and N > nx and ny >= 0 and M > ny:
      if temp[nx][ny] == 0:
        temp[nx][ny] = 2
        spread(nx, ny)

result = 0 

for new in new_walls:
  count = 0
  for wall in new:
    temp[wall[0]][wall[1]] = 1

  for virus in viruses:
    spread(virus[0], virus[1])

  for x in range(N):
    for y in range(M):
      if temp[x][y] == 0:
        count += 1
      temp[x][y] = graph[x][y]
  
  result = max(result, count)  

print(result)

