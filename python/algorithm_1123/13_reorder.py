# https://leetcode.com/problems/reorder-data-in-log-files/
# 로그파일 재정렬 
# 문자열.isalpha() 문자열.isdigit()


class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        letter_log = []
        digit_log = []
        for i in logs:
            if i.split()[1].isalpha():
                letter_log.append(i)
            else:
                digit_log.append(i)
                
        # def temp(log):
        #     return log.split()[1:], log.split()[0]
        # letter_log.sort(key=temp)
        
        letter_log.sort(key = lambda x: (x.split()[1:], x.split()[0])) # x는 letter_log의 요소 하나하나 
            
        return letter_log + digit_log
        
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]

a = Solution()
print(a.reorderLogFiles(logs))