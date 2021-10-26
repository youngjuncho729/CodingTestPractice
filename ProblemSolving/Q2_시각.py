""" 시각
정수 N이 입력되면 00시 00분 00초 부터 N시 59분 59초까지의 모든 시작 중에서 3 이든
하나라도 포함되는 모든 경우의 수를 구하라

완전 탐색 유형 -> 가능한 모든 경우를 모두 검사하고 탐색한다 (단 데이터 개수가 적을때 예 100만 이하)

입력 예시:
    5    (N)
출력 예시:
    11475
"""
import time

# read input
h = int(input())

start_time = time.time()

result = 0

for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                result += 1

print(result)

end_time = time.time()
print("time :", end_time - start_time)
