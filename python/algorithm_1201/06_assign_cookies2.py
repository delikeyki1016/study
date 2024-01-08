from collections import deque

class Solution:
    def find_content_children(self, g: list[int], s: list[int]) -> int:
        result = 0
        
        if len(g) == 0 or len(s) == 0:
            return result
        
        a = max(len(g), len(s))
        g.sort()
        s.sort()
        g_list = deque(g[:])
        s_list = deque(s[:])
        
        for _ in range(a):
            if len(g_list) == 0 or len(s_list) == 0:
                return result
            
            elif g_list[0] <= s_list[0]:
                print(g_list[0], s_list[0])
                result += 1
                g_list.popleft()
                s_list.popleft()
                print('result', result)

            else:
                s_list.popleft()
        
        return result

sol = Solution()
g = [1,2,3]
s = [1,2]
result = sol.find_content_children(g, s)
print(result)