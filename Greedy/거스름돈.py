""" Coin Change Problem"""
""" Minimum number of coins """

n = 1270
count = 0

# check the coin in the descending order
list = [500, 100, 50, 10]

for coin in list:
  count += n // coin # max number of this coin 
  n = n % coin 

print(count)