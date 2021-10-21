def check(answer):
  for x, y, build_type in answer:
    if build_type == 0:
      if y == 0 or [x, y - 1, 0] in answer or [x - 1, y, 1] in answer or [x, y, 1] in answer:
        continue
      else:
        return False
    if build_type == 1:
      if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
        continue
      else:
        return False
  return True


def solution(n, build_frame):
  answer = []
  for build in build_frame:
    x, y, build_type, todo = build
    if todo == 0: #remove this building
      answer.remove([x, y, build_type])
      if not check(answer):
        answer.append([x, y, build_type])
    if todo == 1: #add this building
      answer.append([x, y, build_type])
      if not check(answer):
        answer.remove([x, y, build_type])
  return sorted(answer)

n = 5
build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
build_frame2  =[[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]
print(solution(n, build_frame2))