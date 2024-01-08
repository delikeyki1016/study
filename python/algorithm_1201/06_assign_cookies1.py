class Solution:
    def find_content_children(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        
        result = 0
        kid_index, cookie_index = 0, 0
        
        while kid_index < len(g) and cookie_index < len(s):
            if s[cookie_index] >= g[kid_index]:
                result += 1
                kid_index += 1
            cookie_index += 1
        return result
            

sol = Solution()
g = [1,2,3]
s = [1,2]
result = sol.find_content_children(g, s)
print(result)