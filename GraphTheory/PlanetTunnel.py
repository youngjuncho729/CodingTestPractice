# https://www.acmicpc.net/problem/2887


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


n = int(input())
parent = [i for i in range(n)]
data = []
planet = []

for i in range(n):
    x, y, z = list(map(int, input().split()))
    planet.append((x, y, z, i))

for num in range(3):
    planet.sort(key=lambda x: x[num])
    for i in range(n - 1):
        cost = min(abs(planet[i][0] - planet[i + 1][0]),
                   abs(planet[i][1] - planet[i + 1][1]),
                   abs(planet[i][2] - planet[i + 1][2]))
        data.append((cost, planet[i][3], planet[i + 1][3]))
data.sort()

result = 0
count = 0
for tunnel in data:
    cost, x, y = tunnel
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += cost
        count += 1
    if count == n - 1:
        break
print(result)