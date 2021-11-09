def binary_search_recursive(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  if array[mid] == target:
    return mid
  elif array[mid] > target:
    return binary_search_recursive(array, target, start, mid - 1)
  else:
    return binary_search_recursive(array, target, mid + 1, end)

def binary_search_loop(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None

  

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search_loop(array, target, 0, n - 1)
if result == None:
  print("target is not in the list")
else:
  print(result + 1)