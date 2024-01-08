# https://leetcode.com/problems/assign-cookies/

class Solution:
    def find_content_children(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        
        result = 0
        for kid in g:
            for cookie in s:  # 쿠키 반복
                if kid <= cookie:
                    result += 1
                    s.remove(cookie)
                    print(f"욕심의 크기가 {kid}인 아이에게 {cookie} 크기의 과자를 줍니다.")
                    break
        return result
            

sol = Solution()
g = [1,2,3] # child
s = [1,2] # cookie
result = sol.find_content_children(g, s)
print(result)
