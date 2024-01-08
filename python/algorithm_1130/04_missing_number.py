# https://leetcode.com/problems/missing-number/
# 0~N개의 리스트에서 주어진 리스트에 없는 값 찾기

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # 정렬하고 찾기
        # nums.sort()
        # for i, v in enumerate(nums):
        #     if i != v: # 만약 index와 해당index값이 다르다면 빠진숫자는 i일 것이다.
        #         return i
        # return len(nums)
        
        # 정렬안하고 찾기 => 속도 느림 
        # for i in range(len(nums)+1):
        #     if i not in nums:
        #         return i
            
        # 정렬안하고 찾기, 우왕 
        n = len(nums)
        total = (n * (n + 1)) // 2
        print(total)
        result = total - sum(nums)
        return result
    
sol = Solution()
nums = [9,6,4,2,3,5,7,0,1]
print(sol.missingNumber(nums))