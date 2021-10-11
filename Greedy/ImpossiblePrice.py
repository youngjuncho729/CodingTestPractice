# key point: if n - 1 is possible then can we make n with next coin

n = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1

for i in coins:
  if target < i:
    break
  target += i
print(target)
  
