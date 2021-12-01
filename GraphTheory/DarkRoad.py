# https://www.acmicpc.net/problem/6497


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [i for i in range(n)]
data = []
for _ in range(m):
    data.append(list(map(int, input().split())))

data.sort(key=lambda x: x[2])

result = 0
total = 0
for road in data:
    x, y, cost = road
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += cost
    total += cost
print(total - result)
