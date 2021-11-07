def solution(N, stages):
    players = len(stages)
    fail_rate = []
    for i in range(1, N + 1):
        player_at_i = stages.count(i)
        if players == 0:
          rate = 0
        else:
          rate =  player_at_i / players
        fail_rate.append((i, rate))
        players -= player_at_i
    
    fail_rate.sort(key = lambda x : -x[1])
    result = [i[0] for i in fail_rate]
    return result

print(solution(5 , [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))