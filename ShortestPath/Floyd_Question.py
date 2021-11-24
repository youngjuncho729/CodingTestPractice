# https://www.acmicpc.net/problem/11404
import sys

input = sys.stdin.readline
n, m = int(input()), int(input())
INF = int(1e9)
cities = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            cities[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    cities[a][b] = min(cities[a][b], c)

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            cities[a][b] = min(cities[a][b], cities[a][k] + cities[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if cities[a][b] == 1e9:
            print(0, end=" ")
        else:
            print(cities[a][b], end=" ")
    print()
