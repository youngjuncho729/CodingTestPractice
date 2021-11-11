# https://www.acmicpc.net/problem/2110
import sys
input = sys.stdin.readline
N, C = map(int, input().split())
houses = []
for _ in range(N):
  houses.append(int(input()))
houses.sort()

start = 1 # smallest gap
end = houses[-1] - houses[0] # biggest gap

result = 0
while start <= end:
  mid = (start + end) // 2
  x = houses[0]
  modem = 1
  for i in range(1, N):
    if houses[i] >= x + mid:
      x = houses[i]
      modem += 1
  if modem >= C:
    start = mid + 1
    result = mid
  else:
    end = mid - 1

print(result)