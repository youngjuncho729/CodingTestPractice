# https://www.acmicpc.net/problem/19237
# Samsung 2020

import sys

input = sys.stdin.readline

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

n, m, k = map(int, input().split())
graph = []
smell = [[[0, 0]] * n for _ in range(n)]
exist = [True] * (m + 1)
exist[0] = False  # index 0 for the convenience
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            smell[i][j] = [graph[i][j], k]
direction = [0]
direction.extend(list(map(int, input().split())))
rule = [[] for _ in range(m + 1)]
for i in range(1, m + 1):
    rule[i].append([])
    for j in range(4):
        rule[i].append(list(map(int, input().split())))


def find_shark(graph, index):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == index:
                return (i, j)
    return None


def smell_decrease(smell):
    for i in range(n):
        for j in range(n):
            if smell[i][j][0] != 0:
                smell[i][j][1] -= 1
                if smell[i][j][1] == 0:
                    smell[i][j] = [0, 0]


def get_possible_move(smell, index, x, y):
    empty_smell = []
    my_smell = []
    for direc in rule[index][direction[index]]:
        nx = x + dx[direc]
        ny = y + dy[direc]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if smell[nx][ny][0] == 0:
            empty_smell.append(((nx, ny), direc))
        if smell[nx][ny][0] == index:
            my_smell.append(((nx, ny), direc))
    if len(empty_smell) != 0:
        return empty_smell
    else:
        return my_smell


count = 0
while True:
    count += 1
    new_smell = []
    shark_move = []
    for shark in range(1, m + 1):
        position = find_shark(graph, shark)
        if position != None:
            poss = get_possible_move(smell, shark, position[0], position[1])
            x, y, direc = poss[0][0][0], poss[0][0][1], poss[0][1]
            direction[shark] = direc
            graph[position[0]][position[1]] = 0
            shark_move.append((x, y, shark))
            new_smell.append((x, y, shark))

    for move in shark_move:
        x, y, shark = move
        # remove shark if lower shark is at this position
        if graph[x][y] != 0:
            exist[shark] = False
        else:
            graph[x][y] = shark

    smell_decrease(smell)  # decrease all smell by 1

    # Add new smell created by moving shark
    for new in new_smell:
        if exist[new[2]] == True:
            smell[new[0]][new[1]] = [new[2], k]

    # end if only first shark exists in graph
    if exist.count(True) == 1:  
        print(count)
        break

    # end if it takes over 1000 seconds
    if count >= 1000:
        print(-1)
        break
