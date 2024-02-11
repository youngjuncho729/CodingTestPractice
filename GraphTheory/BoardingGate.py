def mySolution():
  gate_num = int(input())
  planes = int(input())
  gates = [0] * (gate_num + 1)
  possible = [0] * (planes + 1)
  for i in range(planes):
    possible[i] = int(input())
  print(possible)
  for plane in range(1, planes + 1):
    docking = False
    for gate in range(possible[plane], 0, -1):
      if gates[gate] == 0:
        gates[gate] = 1
        docking = True
    if docking == False:
      print(plane)
      break

  if docking == True:
    print(planes)

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

def solution():
  gate_num = int(input())
  planes = int(input())
  parent = [i for i in range(gate_num + 1)]

  result = 0
  for _ in range(planes):
    data = find_parent(parent, int(input()))
    if data == 0:
      break
    union_parent(parent, data, data - 1)
    result += 1
  print(result)

solution()
