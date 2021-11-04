import sys
import copy
from itertools import combinations
input = sys.stdin.readline

N = int(input())
table = []
teachers = []
students = []
obstacles = []
for i in range(N):
  table.append(list(input().split()))
  for j in range(N):
    if table[i][j] == 'T':
      teachers.append((i, j))
    if table[i][j] == 'S':
      students.append((i, j))
    if table[i][j] == 'X':
      obstacles.append((i, j))      
temp = copy.deepcopy(table)

def watch(teachers, temp):
  for x, y in teachers:
    for i in range(1, N):
      if x + i >= N or temp[x + i][y] == 'O':
        break
      if temp[x + i][y] == 'S':
        return False
    for i in range(1, N):
      if y + i >= N or temp[x][y + i] == 'O':
        break
      if temp[x][y + i] == 'S':
        return False
    for i in range(1, N):
      if x - i < 0 or temp[x - i][y] == 'O':
        break
      if temp[x - i][y] == 'S':
        return False
    for i in range(1, N):
      if y - i < 0 or temp[x][y - i] == 'O':
        break
      if temp[x][y - i] == 'S':
        return False
  return True

result = False
obs_combo = list(combinations(obstacles, 3))
for combo in obs_combo:
  for obs in combo:
    temp[obs[0]][obs[1]] = 'O'
  result = watch(teachers, temp)
  if result:
    break
  temp = copy.deepcopy(table)

if result:
  print("YES")
else:
  print("NO")