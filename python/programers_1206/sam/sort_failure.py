def solution(N, stages):
    answer = []
    failure = {}
    arrive_players = len(stages)
    for i in range(1, N + 1):
        if arrive_players != 0:
            count = stages.count(i)
            failure[i] = count / arrive_players
            arrive_players -= count
        else :
            failure[i] = 0
    print(failure)
    answer = sorted(failure, key=lambda x: failure[x], reverse=True)
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))