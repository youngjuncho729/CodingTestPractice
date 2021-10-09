import time
start = time.time()

data = input()

count_1 = 0
count_0 = 0

if data[0] == '1':
  count_0 += 1
else:
  count_1 += 1

for i in range(len(data)-1):
  if data[i] == '1' and data[i + 1] == '0':
    count_0 += 1
  elif data[i] == '0' and data[i + 1] == '1':
    count_1 += 1
  
 

print(min(count_1, count_0))
print("time :", time.time() - start)