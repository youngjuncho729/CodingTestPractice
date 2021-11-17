#Longest Increasing Subsequence
"""
# O(N^2)
# https://www.acmicpc.net/problem/11053
x = int(input())
arr = list(map(int, input().split()))
dp = [1 for i in range(x)]
for i in range(x):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
"""
""" Find the length of LIS but can't find the list of LIS numbers
# O(NlogN)
# https://www.acmicpc.net/problem/12015
#https://www.acmicpc.net/problem/12738

from bisect import bisect_left

n = int(input())
data = list(map(int, input().split()))
dp = [data[0]]
for i in range(n):
    if data[i] > dp[-1]:
        dp.append(data[i])
    else:
        index = bisect_left(dp, data[i])
        dp[index] = data[i]
print(len(dp))
"""
"""
# https://www.acmicpc.net/problem/14002
# https://www.acmicpc.net/problem/14003
n = int(input())
data = list(map(int, input().split()))
dp = [1 for i in range(n)]
for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
lis = []
index = max(dp)
for i in range(n - 1, -1, -1):
    if dp[i] == index:
        lis.append(data[i])
        index -= 1
lis.reverse()
print(*lis)
"""
# https://www.acmicpc.net/problem/14003
from bisect import bisect_left

n = int(input())
data = list(map(int, input().split()))
dp_num = [(data[0], 0)]
dp_rank = [1 for i in range(n)]
for i in range(1, n):
    if data[i] > dp_num[-1][0]:
        dp_rank[i] = dp_rank[dp_num[-1][1]] + 1
        dp_num.append((data[i], i))
    else:
        index = bisect_left(dp_num, (data[i], 0))
        dp_rank[i] = dp_rank[dp_num[index][1]]
        dp_num[index] = (data[i], i)
print(max(dp_rank))

lis = []
index = max(dp_rank)
for i in range(n - 1, -1, -1):
    if dp_rank[i] == index:
        lis.append(data[i])
        index -= 1
lis.reverse()
print(*lis)
