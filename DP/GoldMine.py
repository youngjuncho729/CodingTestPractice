def my_solution():
    T = int(input())
    for i in range(T):
        n, m = map(int, input().split())
        data = list(map(int, input().split()))
        mine = [[] for _ in range(m)]
        for i in range(len(data)):
            mine[i % m].append(data[i])
        gold = max(mine[0])
        now = mine[0].index(gold)
        for i in range(1, m):
            if now - 1 < 0 and now + 1 >= n:
                max_gold = mine[i][now]
            if now - 1 < 0 and now + 1 < n:
                max_gold = max(mine[i][now], mine[i][now + 1])
            if now - 1 >= 0 and now + 1 >= n:
                max_gold = max(mine[i][now - 1], mine[i][now])
            if now - 1 >= 0 and now + 1 < n:
                max_gold = max(mine[i][now - 1], mine[i][now],
                               mine[i][now + 1])
            gold += max_gold
            now = mine[i].index(max_gold)
        print(gold)

def DP_solution():
    for tc in range(int(input())):
        n, m = map(int, input().split())
        data = list(map(int, input().split()))
        index = 0
        mine = []
        for i in range(n):
            mine.append(data[index:index + m])
            index = index + m
        for j in range(1, m):
          for i in range(n):
            if i == 0:
              left_up = 0
            else:
              left_up = mine[i - 1][j - 1]
            if i == n - 1:
              left_down = 0
            else:
              left_down = mine[i + 1][j - 1]
            left = mine[i][j - 1]
            mine[i][j] = mine[i][j] + max(left_down, left, left_up)
        print(max([mine[x][m - 1] for x in range(n)]))

DP_solution()

""" Input
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""
