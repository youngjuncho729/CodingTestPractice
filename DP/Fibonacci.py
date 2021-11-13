# Top Down
d = [0] * 100
def fibo_recursive(x):
  if x == 1 or x == 2:
    return 1
  if d[x] != 0:
    return d[x]
  d[x] = fibo_recursive(x - 1) + fibo_recursive(x - 2)
  return d[x]

print(fibo_recursive(99))

# Bottom Up
d = [0] * 100
d[1] = 1
d[2] = 1
n = 99
for i in range(3, n + 1):
  d[i] = d[i - 1] + d[i - 2]
print(d[i])