#https://www.acmicpc.net/problem/14501
n = int(input())
T = []
P = []
for _ in range(n):
  t, p = map(int, input().split())
  T.append(t)
  P.append(p)
best = [0] * (n + 1)

for i in range(n):
  best[i] = max(best[i], best[i - 1])
  if i + T[i] <= n:
    best[i + T[i]] = max(best[i + T[i]], best[i] + P[i]) 

print(max(best))