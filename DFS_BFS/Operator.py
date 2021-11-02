import sys

input = sys.stdin.readline
N = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_num = -pow(10, 9)
min_num = pow(10, 9)


def dfs(i, result):
    global max_num, min_num, add, sub, mul, div
    if i == N:
        max_num = max(max_num, result)
        min_num = min(min_num, result)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, result + numbers[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, result - numbers[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, result * numbers[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(result / numbers[i]))
            div += 1


dfs(1, numbers[0])
print(max_num)
print(min_num)
""" Slower 
import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
data = list(map(int, input().split()))
operater_number = []
for i in range(4):
  if i == 0 and data[i] != 0:
    operater_number.extend(['+'] * data[i])
  if i == 1 and data[i] != 0:
    operater_number.extend(['-'] * data[i])
  if i == 2 and data[i] != 0:
    operater_number.extend(['*'] * data[i])
  if i == 3 and data[i] != 0:
    operater_number.extend(['/'] * data[i])

max_num = -pow(10, 9)
min_num = pow(10, 9)
for combo in list(permutations(operater_number)):
  result = numbers[0]
  for i, oper in enumerate(combo):
    if oper == '+':
      result = result + numbers[i + 1]
    if oper == '-':
      result = result - numbers[i + 1]
    if oper == '*':
      result = result * numbers[i + 1]
    if oper == '/':
      if result < 0:
        result =  -result
        result = result // numbers[i + 1]
        result =  -result
      else:
        result = result // numbers[i + 1] 
  max_num = max(max_num, result)
  min_num = min(min_num, result)

print(max_num)
print(min_num)
"""
