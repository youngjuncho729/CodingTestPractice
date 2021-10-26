""" 상하좌우 구현 유형 문제
N * N 크기의 공간에서의 움직인 후의 좌표를 출력
L: left 1 space
R: right ...
U: up ...
D: down ...

입렵 예시:
    5  (N)
    R R R U D D
"""
import time


# read inputs
n = int(input())
x, y = 1, 1  # initial coordinate
plans = input().split()

start_time = time.time()

# movements corresponding L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# check each plan
for plan in plans:
    i = move_types.index(plan)
    new_x = x + dx[i]
    new_y = y + dy[i]
    # check the boundary of new coordinate
    if new_x < 1 or n < new_x or new_y < 1 or n < new_y:
        continue  # ignore the movement
    x = new_x
    y = new_y

print(x, y)

end_time = time.time()
print("time :", end_time - start_time)
