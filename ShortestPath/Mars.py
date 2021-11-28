"""
화성 탐사 기계가 출발 지점에서 목표 지점까지 이동할 때 항상 최적의 경로를 찾도록 개발해야 합니다.

화성 탐사 기계가 존재하는 공간은 N x N 크기의 2차원 공간이며, 각각의 칸을 지나기 위한 비용이 존재합니다.

가장 왼쪽 위 칸인 [0][0] 위치에서가장 오른쪽 아래 칸인 [N - 1][N - 1] 위치로 이동하는 최소 비용을 출력하는 프로그램을 작성하세요.

화성 탐사 기계는 특정한 위치에서 상하좌우 인접한 곳으로 1칸씩 이동할 수 있습니다.
"""
import sys
import heapq

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

INF = int(1e9)
input = sys.stdin.readline
cases = int(input())
for _ in range(cases):
    n = int(input())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))

    distance = [[INF] * (n) for _ in range(n)]

    x, y = 0, 0
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]

    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    print(distance[n - 1][n - 1])