# 세 수의 합이 0이 되는 3개의 엘리멘트를 모두 출력 https://leetcode.com/problems/3sum/

class Solution:
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        
        # 1번 방식  
        # result = []
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 temp = [nums[i], nums[j], nums[k]]
        #                 temp.sort()
        #                 if temp not in result:
        #                     result.append(temp)
        # return result
    
    
        # 2번 방식
        # result = []
        # nums.sort()
        # for i in range(len(nums) - 2):
        #     if i > 0 and nums[i] == nums[i - 1]: # [-1, -1, -1, 0, 1, 2] 로 테스트
        #         continue
        #     for j in range(i + 1, len(nums) - 1):
        #         if j > i + 1  and nums[j] == nums[j - 1]:
        #             continue
        #         for k in range(j + 1, len(nums)):
        #             if k > j + 1 and nums[k] == nums[k - 1] :
        #                 continue
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 result.append([nums[i], nums[j], nums[k]])
        # return result        
        
        
        # 3번 방식 
        result = []
        nums.sort()        
        print(nums) #[-4, -1, -1, 0, 1, 2]
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:  
                continue
            lt = i + 1
            rt = len(nums) - 1
            while lt < rt:
                temp_sum = nums[i] + nums[lt] + nums[rt]
                if 0 == temp_sum:
                    result.append([nums[i], nums[lt], nums[rt]])
                    while lt < rt and nums[lt] == nums[lt+1]:
                        lt += 1
                    while lt < rt and nums[rt] == nums[rt-1]:
                        rt -= 1
                    lt += 1
                    rt -= 1
                elif 0 < temp_sum:
                    rt -= 1
                elif 0 > temp_sum:
                    lt += 1
        return result


nums = [-1,0,1,2,-1,-4]
# # Output: [[-1,-1,2],[-1,0,1]]
# nums = [-1, -1, -1, 0, 1, 2] # Output: [[-1, -1, 2], [-1, 0, 1]]
a = Solution()
print(a.three_sum(nums))