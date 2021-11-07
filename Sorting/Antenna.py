N = int(input())
houses = list(map(int, input().split()))
houses.sort()
print(houses[(N - 1) // 2])

""" 시간 초과
N = int(input())
houses = list(map(int, input().split()))
result = -1
short = int(1e9)
for antenna in houses:
  distance = 0
  for house in houses:
    distance += abs(antenna - house)
  if short > distance:
    short = distance
    result = antenna
print(result)
"""