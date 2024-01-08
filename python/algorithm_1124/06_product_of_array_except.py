# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def product_except_self(self, nums: list[int]) -> list[int]:
        
        result = [1] * len(nums)
        print(result) #[1,1,1,1]
        p = 1
        for i in range(len(nums) - 1):
            # print(i)
            p *= nums[i]
            result[i+1] *= p
        # print(result)
        
        p = 1
        for i in range(len(nums)-1, 0, -1):
            p *= nums[i]
            # print(i, nums[i], p)
            result[i-1] *= p
            # print(result)
        return result
    
sol = Solution()
nums = [1,2,3,4]
result = sol.product_except_self(nums)
print(result) #[24,12,8,6]

#         / 1    / 1, 2 / 1, 2, 3
# 2, 3, 4 / 3, 4 / 4    / 