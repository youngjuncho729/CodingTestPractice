# https://www.acmicpc.net/problem/1715
# Key: Choose smallest 2 cards sets every time
import sys
import heapq
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
  heapq.heappush(lst, int(input()))

count = 0
card_1 = 0
while len(lst) > 0:
  if card_1 == 0:
    card_1 =  heapq.heappop(lst)
  else:
    min_sum = card_1 + heapq.heappop(lst)
    heapq.heappush(lst, min_sum)
    card_1 = 0
    count += min_sum
print(count)
