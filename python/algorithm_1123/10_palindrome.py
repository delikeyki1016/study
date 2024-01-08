import re

str = "A man, a plan, a canal:Panama"

# 방법1. 리스트로 변환
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s_list = [i for i in s.lower() if i != ',' and i != ' ' and i != ':']
#         if s_list.pop(0) != s_list.pop():
#             return False
#         else:
#             return True
    
# sol = Solution()
# print(sol.isPalindrome(str)) 


# 방법2. deque 
from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_list = deque([char.lower() for char in s if char.isalnum()])  # isalnum : 영어,한글,숫자이면 트루 
        while len(str_list) > 1:
            if str_list.popleft() != str_list.pop(): #deque의 popleft, pop은 O(1)이다 
                return False
        return True
    
sol = Solution()
print(sol.isPalindrome(""))


# 방법3. 정규표현식을 이용한 슬라이싱 
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = re.sub("[^a-z0-9]", "", s.lower())
#         if s == s[::-1]: # s[:].reverse 한 것과 같다.
#             return True
#         else:
#             return False
    
# sol = Solution()
# print(sol.isPalindrome(str)) 