# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        letter_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        result = []
        word = ""
        
        if digits == "":
            return result
        
        def dfs(word):
            # 입력값(digits)의 길이와 word의 길이를 비교해서 같으면 백트래킹
            if len(word) == len(digits):
                result.append(word)
                return
            # 입력값(digits)에 대한 딕셔너리 내 리스트를 확인
            # 1인 경우에는 [2, 3, 4]
            for i in letter_dict[digits[len(word)]]:
                dfs(word + i) # word에 문자가 하나씩 추가되고, 재귀 호출
        dfs(word)
        return result

sol = Solution()
digits = "23"
result = sol.letterCombinations(digits)
print(result)