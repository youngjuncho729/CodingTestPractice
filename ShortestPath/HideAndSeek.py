"""
동빈이는 숨바꼭질을 하면서 술래로부터 잡히지 않도록 숨을 곳을 찾고 있다. 동빈이는 1 ~ N번까지의 헛간 중에서 하나를 골라 숨을 수 있으며, 술래는 항상 1번 헛간에서 출발한다. 전체 맵에는 총 M개의 양방향 통로가 존재하며, 하나의 통로는 서로 다른 두 헛간을 연결한다. 또한 전체 맵은 항상 어떤 헛간에서 다른 어떤 헛간으로 도달이 가능한 형태로 주어진다.

동빈이는 1번 헛간으로부터 최단 거리가 가장 먼 헛간이 가장 안전하다고 판단하고 있다. 이 때 최단 거리의 의미는 지나야 하는 길의 최소 개수를 의미한다. 동빈이가 숨을 헛간의 번호를 출력하는 프로그램을 작성해라.
"""

import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline
n, m = map(int, input().split())
distance = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

q = []
heapq.heappush(q, (0, 1))
distance[1] = 0
while q:
  dist, now = heapq.heappop(q)
  if dist < distance[now]:
    continue
  for adj in graph[now]:
    cost = dist + 1
    if cost < distance[adj]:
      distance[adj] = cost
      heapq.heappush(q, (cost, adj))

max_dist = max(distance[1:])
print(distance[1:].index(max_dist) + 1, max_dist, distance[1:].count(max_dist))