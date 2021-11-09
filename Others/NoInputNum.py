# https://www.acmicpc.net/problem/10951
# When number of input is not given

while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break