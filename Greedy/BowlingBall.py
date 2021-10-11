num_ball, max_weight = map(int, input().split())
data = list(map(int, input().split()))

weight_list = [0] * (max_weight + 1)
for ball in data:
  weight_list[ball] += 1
  
print(weight_list)

result = 0

"""
# My Solution
for x in range(1, max_weight):
    for y in range(x + 1, max_weight + 1):
      result += weight_list[x] * weight_list[y]
      print("x: ", weight_list[x], " y: ", weight_list[y], "result: ", result)
"""

# Book Solution
for i in range(1, max_weight + 1):
  num_ball -= weight_list[i] # Exept weight i ball from total number
  result += weight_list[i] * num_ball

print(result)