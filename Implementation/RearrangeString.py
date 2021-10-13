n = input()

num_sum = 0
char = []

for i in range(len(n)):
  if n[i].isnumeric():
    num_sum += int(n[i])
  else:
    char.append(n[i])

char.sort()
print(''.join(char), end = '')
print(num_sum)