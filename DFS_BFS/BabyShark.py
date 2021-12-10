# https://www.acmicpc.net/problem/16236
# Samsung 2020 Quesiton using BFS

import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)
n = int(input())
data = []
shart = (0, 0)
for i in range(n):
    line = list(map(int, input().split()))
    if 9 in line:
        shark = (i, line.index(9))
    data.append(line)
data[shark[0]][shark[1]] = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def BFS(x, y, size):
    q = deque()
    q.append((x, y, 0))  # coordinates and distance from starting position
    can_eat = []
    graph = [[INF] * n for _ in range(n)]
    graph[x][y] = 0
    while q:
        x, y, cost = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if data[nx][ny] > size or graph[nx][ny] != INF:
                continue
            graph[nx][ny] = cost + 1
            if 0 < data[nx][ny] < size:
                can_eat.append((nx, ny, graph[nx][ny]))
            q.append((nx, ny, graph[nx][ny]))

    if len(can_eat) == 0:
        return (-1, -1, 0)
    else:
        can_eat.sort(key=lambda x: (x[2], x[0], x[1]))
        return can_eat[0]


result = 0
size = 2  # initial size of the shark
ate = 0  # number of fish ate at this size
x, y, cost = BFS(shark[0], shark[1], size)
while (x, y) != (-1, -1):
    data[x][y] = 0
    result += cost
    ate += 1
    if ate == size:
        ate = 0
        size += 1
    x, y, cost = BFS(x, y, size)
print(result)