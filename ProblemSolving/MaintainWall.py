from itertools import permutations
def solution(n, weak, dist):
    answer = int(1e9) #infinity
    length = len(weak)
    # make 2xlist to turn circle shape input into a straight line
    weak = weak + [x + n for x in weak] 

    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            num = 1
            position = weak[start] + friends[num - 1]
            for index in range(start, start + length):
                if position < weak[index]:
                    num += 1
                    if num > len(dist):
                        break
                    position = weak[index] + friends[num - 1]        
            answer = min(answer, num)

    return answer if answer <= len(dist) else -1 



n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
print(solution(n, weak, dist))