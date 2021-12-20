# https://www.acmicpc.net/problem/1759
"""
 This question requires to print all possible password with at least one vowel
 and two consonants.
 -> Use Combination and check the number of vowel and consonants, print if qualified.
"""
from itertools import combinations

l, c = map(int, input().split())
vowels = ['a', 'e', 'i', 'o', 'u']

chars = list(input().split())
chars.sort()
for password in combinations(chars, l):
    count = 0
    for char in password:
        if char in vowels:
            count += 1
    if count >= 1 and len(password) - count >= 2:
        print("".join(password))
