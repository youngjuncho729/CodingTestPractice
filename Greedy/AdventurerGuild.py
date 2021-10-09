# My Solution
n = int(input())
list_adv = list(map(int, input().split()))
#list_adv.sort(reverse = True)

"""
team = 0
while 0 < len(list_adv):
  least = list_adv[0]
  print("least: ", least)
  if len(list_adv) < least:
    break
  least -= 1
  del list_adv[0]
  if least != 0:
    del list_adv[-least: ]
  print(list_adv)
  team += 1

print("max number of guild: ", team)
"""

# Book Solution
list_adv.sort()

result = 0
count = 0

for i in list_adv:
  count += 1
  if count >= i:
    result += 1
    count = 0
print(result)