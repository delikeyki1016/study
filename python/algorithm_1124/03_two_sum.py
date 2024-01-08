# 리스트 중에 두개의 요소의 합이 타겟이 되는 해당 요소의 인덱스를 구하기 
# https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        # 방식1. 최대반복 수 n*(n-1)/2 = 6번  brute force 노가다 방식이지만 정확도 높다. 복잡도는 n제곱
        # for i in range(len(nums) - 1): # n-1번 반복
        #     for j in range(i+1, len(nums)): #
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        
        # 방식2. 빠르다.
        # for i, v in enumerate(nums):
        #     gap = target - v
        #     if gap in nums[i+1:]:
        #         # print(nums[i+1:].index(gap))
        #         return [i, i + 1 + nums[i+1:].index(gap)]
        
        # nums = [3,2,4]  and i != nums_dict[gap] 가 필요한 이유
        # target = 6
        # 방식3. 딕셔너리 활용
        # nums_dict = {}
        # for i, v in enumerate(nums):
        #     nums_dict[v] = i
        # print(nums_dict)
        # for i, v in enumerate(nums):
        #     gap = target - v
        #     if gap in nums_dict and i != nums_dict[gap]: # value를 이용 key를 찾는다면 매번 딕셔너리 전체를 순회함!
        #         return [i, nums_dict[gap]]
                    
        # 방식 4. 위의 for를 하나로
        # nums_dict = {}
        # for i, v in enumerate(nums):
        #     gap = target - v
        #     if gap in nums_dict and i != nums_dict[gap]:
        #         return [i, nums_dict[gap]]
        #     nums_dict[v] = i 
        
        # 방식 5 이것은 배열이 정렬이 된 상태라는 전제가 필요하다. 
        lt = 0
        rt = len(nums) - 1
        while lt < rt:
            if nums[lt] + nums[rt] == target:
                return [lt, rt]
            elif nums[lt] + nums[rt] > target:
                rt -= 1
            elif nums[lt] + nums[rt] < target:
                lt += 1

# nums = [3,2,4] #방식4번의 테스트 
# target = 6
nums = [2,7,11,15]
target = 9
a = Solution()
print(a.twoSum(nums, target))