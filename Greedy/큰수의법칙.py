""" 큰수의 법칙
n: number of given numbers
m: number of addition
k: max number of continuously adding same index

input example:
  5 8 3      (n, m, k)
  2 4 5 4 6  (list of numbers)
"""
# first line input
n, m, k = map(int, input().split())
# second line input
data = list(map(int, input().split()))

data.sort()
max1 = data[n - 1]
max2 = data[n - 2]

result = 0

""" Easy Way """
# while True:
#   for i in range(k):
#     if m == 0:
#       break
#     result += max1
#     m -= 1
#   if m == 0:
#     break
#   result += max2
#   m -= 1

""" Faster Way """
# number of adding max1
count = (m // (k + 1)) * k + m % (k + 1)

result = count * max1
result += (m - count) * max2

print("result is " + str(result))
