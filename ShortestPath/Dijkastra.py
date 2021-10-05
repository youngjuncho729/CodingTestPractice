import sys
input = sys.stdin.readline
INF = int(1e9)

# number of nodes and edges
n, m = map(int, input().split())
# starting node
start = int(input())
# create a list of info about adjacent of each node
graph = [[] for i in range(n + 1)]
# either each node is visited or unvisited
visited = [False] * (n + 1)
# set the default distance to INF
distance = [INF] * (n + 1)

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

# Get the unvisited node with shortest distance
def get_smallest_node():
  min_value = INF
  index = 0
  for i in range(1, n + 1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index

def dijkstra(start):
    # reset the starting node
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # repeat each node except the starting node
    for i in range(n - 1):
        # set the shorted distance node to visited
        now = get_smallest_node()
        visited[now] = True
        # Check all adjacent node
        for j in graph[now]:
            cost = distance[now] + j[1]
            # if the path through other node is shorter
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n + 1):
  if distance[i] == INF:
    print("INFINITY")
  else:
    print(distance[i])