from collections import deque 

N = int(input())
K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
turn = []
for _ in range(L):
  x, c = input().split()
  turn.append([int(x), c])
board = [[0] * N for _ in range(N)]
for apple in apples:
  board[apple[0] - 1][apple[1] - 1] = 1

def move(direction, head):
  if direction == "right":
    head[1] += 1
  elif direction == "left":
    head[1] -= 1
  elif direction == "up":
    head[0] -= 1
  else:
    head[0] += 1

def turnHead(direction, turn):
  if direction == "right" and turn == "L" or direction == "left" and turn == "D":
    return "up"
  elif direction == "right" and turn == "D" or direction == "left" and turn == "L":
    return "down"
  elif direction == "up" and turn == "L" or direction == "down" and turn == "D":
    return "left"
  elif direction == "up" and turn == "D" or direction == "down" and turn == "L":
    return "right"

def gameOver(head, body):
  if N <= head[0] or N <= head[1] or head[0] < 0 or head[1] < 0:
    return True
  if head in body:
    return True
  return False

head = [0, 0]  # Coordinate of the snake head
body = deque() # list of snake body coordinate
direction = "right" # starting diretion
sec = 0   # how may seconds after game start
over = False
next_turn = 0   # index of the next turn

while over == False:
  sec += 1
  prev_x, prev_y = head[0], head[1]
    # Eat the apple
  move(direction, head)
  # Check if snake hits the wall or its body
  if gameOver(head, body):
    over = True
  # Make the turn if it needs
  if next_turn < L and turn[next_turn][0] == sec:
    direction = turnHead(direction, turn[next_turn][1])
    next_turn += 1
  # Add the body if snake eats apple
  if 0 <= head[0] < N and 0 <= head[1] < N:
    body.appendleft([prev_x, prev_y])
    if board[head[0]][head[1]] == 1:
      board[head[0]][head[1]] = 0
    else:
      body.pop()
print(sec)