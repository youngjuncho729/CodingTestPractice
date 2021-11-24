# https://www.acmicpc.net/problem/11403

n = int(input())
graph = [[0] * n for _ in range(n)]

for i in range(n):
    path = list(map(int, input().split()))
    for j in range(n):
        graph[i][j] = path[j]

for k in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][b] == 1:
                continue
            graph[a][b] = 1 if graph[a][k] + graph[k][b] == 2 else 0

for a in range(n):
    for b in range(n):
        print(graph[a][b], end=" ")
    print()
