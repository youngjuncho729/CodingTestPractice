# 특정한 합을 가지는 부분 연속 수열 찾기
# can not use two pointers if contains negative number

n = 5  # data size
m = 5  # target sum
data = [1, 2, 3, 2, 5]


def find_target_sum_interval(n, m, data):
    count = 0
    interval_sum = 0
    end = 0

    for start in range(n):
        # increase end to the max
        while interval_sum < m and end < n:
            interval_sum += data[end]
            end += 1
        if interval_sum == m:
            count += 1
        interval_sum -= data[start]

    print(count)


find_target_sum_interval(n, m, data)


# 정렬되어 있는 두 리스트의 합집합
# i points the smallest  in unvisited number of list A
# j points the smallest  in unvisited number of list B
# append min(i, j) into the result

n, m = 3, 4
a = [1, 3, 5]
b = [2, 4, 6, 8]

def union_two_sorted_list(n, m, a, b):
  result = [0] * (n + m)
  i, j, k = 0, 0, 0
  while i < n or j < m:
    if j >= m or (i < n and a[i] <= b[j]):
      result[k] = a[i]
      i += 1
    else:
      result[k] = b[j]
      j += 1
    k += 1
  
  for i in result:
    print(i, end=' ')

union_two_sorted_list(n, m, a, b)