""" 1 이 될 때까지 1번 혹은 2번 과정을 수행하는 최소한의 횟수
1. n 에서 1을 뺀다
2. n 을 k로 나눈다

입력 예시:
    25 5    (n, k)
출력 예시:
    2
"""

n, k = map(int, input().split())

count = 0

""" My Solution"""
# while n != 1:
#     if n % k == 0:
#         n = n / k
#     else:
#         n -= 1
#     count += 1

""" Faster solution for larger input"""
while True:
    # (N == K로 나누어떨어지는 수)가 될떄까지 1씩 빼기
    target = (n // k) * k
    count += (n - target)
    n = target
    # N이 K보다 작을 때(더 이상 나눌 수 없을 떄) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    count += 1
    n //= k

count += (n - 1)

print(count)
