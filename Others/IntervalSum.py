# Use Prefix Sum to find given interval sum in O(N + M)

n = 5
data = [10, 20, 30, 40, 50]

sum_value = 0
prefix_sum = [0]
for i in data:
  sum_value += i
  prefix_sum.append(sum_value)

# find sum of data[3] ~ data[4]
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])