import numpy as np

def rotate(key):
    return np.array(list(zip(*key[::-1])))
    
def check(newlock, n):
    for i in range(n):
        for j in range(n):
            if newlock[n + i][n + j] != 1:
                return False
    return True

def add_key(x, y, m, lock, key):
  for i in range(m):
    for j in range(m):
        lock[x + i][y + j] += key[i][j]

def remove_key(x, y, m, lock, key):
  for i in range(m):
    for j in range(m):
        lock[x + i][y + j] -= key[i][j]

def solution(key, lock):
    n = len(lock)
    m = len(key)
    newlock = np.pad(lock, ((n, n), (n, n)))
 
    rotated_key = key
    for _ in range(4):
        rotated_key = rotate(rotated_key)
        for x in range(n * 2):
            for y in range(n * 2):
                add_key(x, y, m, newlock, rotated_key)
                if check(newlock, n): 
                    return True
                remove_key(x, y, m, newlock, rotated_key)

    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))