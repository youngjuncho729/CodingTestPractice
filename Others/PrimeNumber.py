import math


def is_prime_number(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


"""
 Sieve of Eratosthenes (에라토스테네스의 체)
 Find all primber number in given range
"""


def find_all_prime_number(n):
    is_prime = [True for _ in range(n + 1)]
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i] == True:
            j = 2
            while i * j <= n:
                is_prime[i * j] = False
                j += 1

    for i in range(2, n + 1):
        if is_prime[i] == True:
            print(i, end=' ')

find_all_prime_number(1000)


# https://www.acmicpc.net/problem/1929

def find_all_prime_number(m, n):
    is_prime = [True for _ in range(n + 1)]
    is_prime[0] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i] == True:
            j = 2
            while i * j <= n:
                is_prime[i * j] = False
                j += 1

    for i in range(m, n + 1):
        if is_prime[i] == True:
            print(i)

m, n = map(int, input().split())
find_all_prime_number(m,  n)