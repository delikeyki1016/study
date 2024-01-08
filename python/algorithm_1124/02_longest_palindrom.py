# https://leetcode.com/problems/longest-palindromic-substring/
# 가장 긴 팰린드롬 찾기 

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                temp = s[i:j+1]
                print(temp, temp[::-1])
                if len(temp) > len(result):
                    if temp == temp[::-1]:
                        result = temp
                        print('result',result)
        return result

str = "babad"
a = Solution()
print(a.longestPalindrome(str))