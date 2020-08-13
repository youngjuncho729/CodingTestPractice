""" 숫자카드게임
n * m 카드중에 각행 제일 작은 숫자중 가장 큰수 찾기
입렵 예시:
    3 3     (행의 개수, 열수의 개수)
    3 1 2
    4 1 4
    2 2 2
출력 예시:
    2
"""

n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    result = max(result, min(data))

print(result)
