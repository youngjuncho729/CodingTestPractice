def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, x, y):
  a = find_parent(parent, x)
  b = find_parent(parent, y)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b
  
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

edges = []
for i in range(n):
  edge = list(map(int, input().split()))
  for j in range(n):
    if edge[j] == 1:
      union_parent(parent, i + 1, j + 1)

plan = list(map(int, input().split()))

for i in range(m - 1):
  if find_parent(parent, plan[i]) != find_parent(parent, plan[i + 1]):
    print("NO")
    break
print("YES")