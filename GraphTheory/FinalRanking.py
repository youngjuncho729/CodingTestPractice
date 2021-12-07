# https://www.acmicpc.net/problem/3665
# This question requires to find the correct ordering of teams by looking at last year's ranking and the changes in the ranking this year -> Topological Sort

import sys
from collections import deque

input = sys.stdin.readline
cases = int(input())

for _ in range(cases):
    n = int(input())
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    last_year = list(map(int, input().split()))
    for i in range(n - 1):
        for j in range(i + 1, n):
            graph[last_year[i]].append(last_year[j])
            indegree[last_year[j]] += 1

    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        if b in graph[a]:
            indegree[a] += 1
            indegree[b] -= 1
            graph[b].append(a)
            graph[a].remove(b)
        else:
            indegree[a] -= 1
            indegree[b] += 1
            graph[a].append(b)

    result = []
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    cycle = False
    duplicate = False

    for i in range(n):
        if len(q) == 0:
            cycle = True
            break
        if len(q) >= 2:
            duplicate = True
            break
        now = q.popleft()
        result.append(now)
        for team in graph[now]:
            indegree[team] -= 1
            if indegree[team] == 0:
                q.append(team)

    if cycle:
        print("IMPOSSIBLE")
    elif duplicate:
        print("?")
    else:
        for team in result:
            print(team, end=' ')
        print()