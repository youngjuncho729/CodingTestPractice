N = int(input())
array = list(map(int, input().split()))

def find_fixed_point(array, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == mid:
      return mid
    elif array[mid] < mid:
      start = mid + 1
    else:
      end = mid - 1
  return -1

print(find_fixed_point(array, 0, N - 1))