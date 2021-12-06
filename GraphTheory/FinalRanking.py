# https://www.acmicpc.net/problem/3665
# This question requires to find the correct ordering of teams by looking at last year's ranking and the changes in the ranking this year -> Topological Sort

import sys

input = sys.stdin.readline
cases = int(input())

for _ in range(cases):
    n = int(input())
    
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    last_year = list(map(int, input().split()))
    m = int(input())  

