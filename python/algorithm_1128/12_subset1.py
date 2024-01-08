nums = [1, 2, 3]

def subset(nums):
    results=[]
    subset=[]
    index = 0
    def dfs(idx, subset):
        results.append(subset)
        for i in range(idx, len(nums)):
            new_subset = subset[:]
            new_subset.append(nums[i])
            print(new_subset)
            dfs(i+1, new_subset)
    dfs(index, subset)
    print(results)

subset(nums)
# 결과 = [] 
# 부분집합 = []

# 결과 = [[]]  공집합 선 추가
# 리스트 전체[1,2,3]를 반복
# 1. 0번째 [1]
#     부분집합 = [1]
#     결과 = [[], [1]]
#     리스트 일부[2,3]를 반복
#     1. [2]
#         부분집합 = [1, 2]
#         결과 = [[], [1], [1, 2]]
#         리스트 일부[3]를 반복
#             1. [3]
#             부분집합 = [1, 2, 3]
#             결과 = [[], [1], [1, 2], [1, 2, 3]]
#     2. [3]
#         부분집합 = [1, 3]
#         결과 = [[], [1], [1, 2], [1, 2, 3], [1, 3]]
# 2. 1번째 [2]
#     부분집합 = [2]
#     결과 = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2]]
# 3. 2번째 [3]
#     부분집합 = [3]
#     결과 = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2,3], [3]]