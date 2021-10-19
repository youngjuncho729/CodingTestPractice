def solution(n, build_frame):
  answer = [[]]
  board = [[-1] * n for _ in range(n)]
  print(board)
  return answer


n = 5
build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
print(solution(n, build_frame))