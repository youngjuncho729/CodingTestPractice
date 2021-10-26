num_list = list(map(int, input()))

left_sum = 0
right_sum = 0

for i in range(0, len(num_list) // 2):
  left_sum += num_list[i]
  right_sum += num_list[len(num_list) - 1 - i]

if left_sum == right_sum:
  print("LUCKY")
else:
  print("READY")