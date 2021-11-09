from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
list = list(map(int, input().split()))
left = bisect_left(list, x)
right = bisect_right(list, x)

print(right - left if right - left != 0 else -1)
