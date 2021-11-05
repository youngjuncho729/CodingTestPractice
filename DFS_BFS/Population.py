import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())
land = []
for _ in range(N):
    land.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def union(land, x, y, index):
    q = deque()
    q.append((x, y))
    union_list = [(x, y)]
    visited[x][y] = index
    countries = 1
    population = land[x][y]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if N > nx >= 0 and N > ny >= 0 and visited[nx][ny] == -1:
                diff = abs(land[x][y] - land[nx][ny])
                if L <= diff <= R:
                    visited[nx][ny] = index
                    union_list.append((nx, ny))
                    population += land[nx][ny]
                    countries += 1
                    q.append((nx, ny))

    for x, y in union_list:
        land[x][y] = population // countries

count_days = 0
while True:
    visited = [[-1] * N for _ in range(N)]
    index = 0
    for x in range(N):
        for y in range(N):
            if visited[x][y] == -1:
                union(land, x, y, index)
                index += 1
    if index == N * N:
        break
    count_days += 1
print(count_days)
