# 빗물트래핑 https://leetcode.com/problems/trapping-rain-water/submissions/ 

class Solution:
    def trap(self, height: list[int]) -> int:
        lt, rt = 0, len(height) - 1
        max_lt = height[lt]
        max_rt = height[rt]
        
        volume = 0
        while lt < rt:
            if max_lt < max_rt:
                volume += max_lt - height[lt]
                lt += 1
                max_lt = max(max_lt, height[lt])
            else:
                volume += max_rt - height[rt]
                rt -= 1
                max_rt = max(max_rt, height[rt])
        return volume

# height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [0,1,0,2,1,3,0,2]
a = Solution()
print(a.trap(height)) # 6