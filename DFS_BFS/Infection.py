import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
table = []
viruses = []
for i in range(N):
  table.append(list(map(int, input().split())))
  for j in range(N):
    if table[i][j] != 0:
      viruses.append((table[i][j], 0, i, j))
S, X, Y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

viruses.sort()
q = deque(viruses)

def spread(virus_type, s, x, y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= 0 and N > nx and ny >= 0 and N > ny:
      if table[nx][ny] == 0:
        table[nx][ny] = virus_type
        q.append((virus_type, s + 1, nx, ny))

while q:
  now = q.popleft()
  if now[1] == S or table[X - 1][Y - 1] != 0:
    break
  spread(now[0], now[1], now[2], now[3])

print(table[X - 1][Y - 1])

""" 시간 초과
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
table = []
viruses = [[] for _ in range(K + 1)]
for i in range(N):
  table.append(list(map(int, input().split())))
  for j in range(N):
    if table[i][j] != 0:
      viruses[table[i][j]].append((i, j))
S, X, Y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def spread(x, y, infected, virus_type):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= 0 and N > nx and ny >= 0 and N > ny:
      if table[nx][ny] == 0:
        table[nx][ny] = virus_type
        if nx == X and ny == Y:
          return True
        infected.append((nx, ny))
  return False

while S > 0:
  for virus_type, virus in enumerate(viruses):
    infected = []
    for x, y in virus:
      if spread(x, y, infected, virus_type):
        break
    virus.extend(infected)
  S -= 1

print(table[X - 1][Y - 1])
"""