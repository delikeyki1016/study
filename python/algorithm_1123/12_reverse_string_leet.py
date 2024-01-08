# 문자열 뒤집기 https://leetcode.com/problems/reverse-string

class Solution:
    def reverseString(self, s: list[str]) -> None:
        
        # s.reverse()
        import copy
        s_copy = copy.deepcopy(s)
        s_copy = s_copy[::-1]
        # s[::-1] # s = s[s::-1] 이것은 리트코드에 올리면 에러
        
        # left, right = 0, len(s) - 1
        
        # while left < right:
        #     s[left], s[right] = s[right], s[left]
        #     left += 1
        #     right -= 1
        
        print(s_copy)

data = ["h","e","l","l","o"]
a = Solution()
a.reverseString(data)