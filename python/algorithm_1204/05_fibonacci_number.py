# count = 0  # 재귀호출이 28번 
# class Solution:
#     def fib(self, n: int) -> int:
#         # if n == 0:
#         #     return 0
#         # if n == 1:
#         #     return 1
#         global count
#         count += 1
#         print(count)
#         if n <= 1:  # if n in [0, 1]:
#             return n
#         return self.fib(n - 1) + self.fib(n - 2)
    
# sol = Solution()
# result = sol.fib(6)
# print(result)

# 다이나믹 top down (메모이제이션) 56ms 재귀호출 6번으로 횟수 1/4 이상 줄임 
class Solution:
    def fib(self, n: int) -> int:
        def top_down(n: int, memo: list) -> int:
            if n <= 1:
                return n
            elif memo[n] != 0:
                return memo[n]
            memo[n] = top_down(n - 1, memo) + top_down(n - 2, memo)
            print(memo)
            return memo[n]
        memo = [0, 1] + [0] * (n - 1)
        return top_down(n, memo)
    
sol = Solution()
result = sol.fib(6)
print(result)

# 다이나믹 bottom up (타뷸레이션) 29ms 제일 빠름 
class Solution:
    def fib(self, n: int) -> int:
        temp_list = [0, 1]
        if n in temp_list:
            return n
        for i in range(2, n + 1):
            temp_list.append(temp_list[i-1] + temp_list[i-2])
            print(temp_list)
        return temp_list[-1]
    
# sol = Solution()
# result = sol.fib(6)
# print(result)