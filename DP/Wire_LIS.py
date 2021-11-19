# https://www.acmicpc.net/problem/2568
import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
data.sort()
data1 = [x[1] for x in data]
data.sort(key=lambda x: x[1])
data2 = [x[0] for x in data]


def lis(data, n):
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
    return (n - max(dp_rank), dp_rank)


def lis_list(data, dp_rank):
    lis = []
    index = max(dp_rank)
    for i in range(n - 1, -1, -1):
        if dp_rank[i] == index:
            lis.append(data[i])
            index -= 1

    result = [x for x in data if x not in lis]
    for x in sorted(result):
        print(x)


lis_A = lis(data1, n)
lis_B = lis(data2, n)
if lis_A[0] < lis_B[0]:
    print(lis_A[0])
    lis_list(data1, lis_A[1])
else:
    print(lis_B[0])
    lis_list(data2, lis_B[1])
