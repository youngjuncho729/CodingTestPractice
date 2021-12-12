# https://www.acmicpc.net/problem/19236
# Samsung 2020

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

data = [[] for _ in range(4)]
fishes = []
for i in range(4):
    line = list(map(int, input().split()))
    for j in range(4):
        number = line[j * 2]
        direction = line[j * 2 + 1]
        fishes.append([number, direction, i, j])
        data[i].append([number, direction, i, j])
fishes.sort()
print(data)
print(fishes)


def DFS():
    max_fishes = 0

    return max_fishes


result = data[0][0][0]  #Starting at eating first fish at (0, 0)
shark = [0, 0, data[0][0][1]]  # [x, y, direction]
data[0][0] = [-1, -1, 0, 0]

for i in range(2):
    num, direction, x, y = fishes[i]
    for fish_direction in range(direction, direction + 8):
        fish_direction = fish_direction % 8
        if fish_direction == 0: fish_direction = 8
        nx = x + dx[direction - 1]
        ny = y + dy[direction - 1]
        if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
            continue
        if data[nx][ny][0] == -1:  # Shark at this coordinate
            continue
        if data[nx][ny][1] == 0:  # empty at this coordinate
            fishes[i][2], fishes[i][3] = nx, ny
            data[nx][ny] = fishes[i]
            data[x][y][0], data[x][y][1] = 0, 0
        else:  # swap with the fish at the direction
            swap_index = fishes.index(data[nx][ny])
            fishes[i][2], fishes[i][3] = fishes[swap_index][2], fishes[
                swap_index][3]
            fishes[swap_index][2], fishes[swap_index][3] = x, y
            data[x][y], data[nx][ny] = fishes[swap_index], fishes[i]
        break

print("---------after-------------")
print(data)
print(fishes)
