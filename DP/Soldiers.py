# https://www.acmicpc.net/problem/18353
from bisect import bisect_left
n = int(input())
data = list(map(int, input().split()))
data.reverse()

dp = [data[0]]
for i in range(1, n):
  if data[i] > dp[-1]:
    dp.append(data[i])
  else:
    index = bisect_left(dp, data[i])
    dp[index] = data[i]
print(n - len(dp))