from collections import deque
dx = [-1, 0, 1, 0,]
dy = [0, -1, 0, 1,]

def get_next_pos(board, robot):
  next_pos = []
  pos = list(robot)
  pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
  
  for i in range(4):
    next1_x, next1_y, next2_x,next2_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]
    if board[next1_x][next1_y] == 0 and board[next2_x][next2_y] == 0:
      next_pos.append({(next1_x, next1_y), (next2_x, next2_y)})
    if pos1_x == pos2_x:  # Horizontal
      for i in [-1, 1]:
        if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:
          next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
          next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
    if pos1_y == pos2_y: # Vertical
      for i in [-1, 1]:
          if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0:
            next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
            next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})
  return next_pos

def solution(board):
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
      for j in range(n):
        new_board[i + 1][j + 1] = board[i][j]
    robot = {(1, 1), (1, 2)} # Starting point
    q = deque()
    visited = []
    q.append((robot, 0))
    while q:
      pos, count =q.popleft()
      if (n, n) in pos:
        return count
      for next_pos in get_next_pos(new_board, pos):
        if next_pos not in visited:
          q.append((next_pos, count + 1))
          visited.append(next_pos)
    return 0

test = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
print(solution(test))