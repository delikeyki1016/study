def combination_sum(candidates, target):
    results = []
    result = []
    def dfs(idx, target):
        if target < 0:
            return
        elif target == 0:
            results.append(result[:])
            return
        for i in range(idx, len(candidates)):
            result.append(candidates[i])
            new_target = target - candidates[i]
            dfs(i, new_target)
            result.pop()
    dfs(0, target)
    return results

candidates = [2, 3, 6, 7]
target = 7
print(combination_sum(candidates, target))  # [ [7], [2,2,3] ] 썸해서 타겟이 되는 조합 찾기

# [2, 3, 6, 7]을 반복!
# 1. [2]
# target = target - 2
    # [2, 3, 6, 7]을 반복!
    # 1. [2]
    # target = target - 2 !!! 만약 target이 0이면 결과에 저장! (만약 0보다 작으면 중단)
        # [2, 3, 6, 7]을 반복!
        
    # 2. [3]
    # target = target - 3
        # [3, 6, 7]을 반복!
        
    # 3. [6]
    # target = target - 6
        # [6, 7]을 반복!
    # 4. [7]
    # target = target - 7

# 2. [3]
# target = target - 3
    # [3, 6, 7]을 반복!

# 3. [6]
# target = target - 6
    # [6, 7]을 반복!

# 4. [7]
# target = target - 7