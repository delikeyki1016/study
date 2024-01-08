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
        for i in letter_dict[digits[0]]:
            if digits[1]:
                for j in letter_dict[digits[1]]:
                    word = i+j
                    result.append(word)
            else:
                word = i
                result.append(word)
        return result

sol = Solution()
digits = "3"
result = sol.letterCombinations(digits)
print(result)