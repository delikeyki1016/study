# https://leetcode.com/problems/largest-number/
# 양의 정수로 구성된 리스트를 조합하여 가장 큰수를 반환

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        nums = [str(i) for i in nums]        
        nums.sort(key=lambda x:x*9, reverse=True)
        nums = ''.join(nums)
        # if nums[0] == '0':
        #     return '0'
        # else:
        #     return nums
        return str(int(nums)) # [0,0]인 경우는 "00" 이 나오기 때문에, 숫자로 바꾼 후 문자로 바꿔줌 
        
sol = Solution()
nums = [3,30,34,5,9]
print(sol.largestNumber(nums))
