# 짝이 안맞을 때 false 출력
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def is_valid(self, s: str) -> bool:
        stack = []
        mapping = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        
        for i in s:
            if i not in mapping: # 여는 괄호가 들어왔을 때 
                stack.append(i) # 스택에는 여는 괄호가 들어간다.
            # 닫는 괄호가 들어왔는데, 스택에 여는 괄호가 없거나, 짝꿍괄호가 다르면 폴스
            elif not stack or mapping[i] != stack.pop(): # 여기서 pop이 수행이 되버림 
                return False
        return bool(not stack)
                
sol = Solution()
result = sol.is_valid("(){}[]")
print(result)