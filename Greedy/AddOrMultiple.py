import time
start = time.time()
num_list = list(map(int, input()))
print(num_list)

""" 
# Slower
result = num_list[0]
for i in range(1, len(num_list)):
  if num_list[i] <= 1 or result == 0:
    result = result + num_list[i]
  else:
    result = result * num_list[i]

print(result)
print("time :", time.time() - start) # time : 3.770578622817993
"""

result = num_list.pop(0)
for num in num_list:
  if result == 0 or num <= 1:
    result += num
  else:
    result *= num 

print(result)
print("time :", time.time() - start) # time : 2.712271213531494
