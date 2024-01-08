# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# price 배열의 순서대로 주식을 샀다가 팔았다고 했을 때 최대 수익은 얼마인가? 
# 브루트포스는(이중for문) n2이니까 n으로 만드는 방식으로는 최소금액을 기준으로 

class Solution:
    def max_profit(self, prices: list[int]) -> int:
        # 현재 최소금액을 구한다. 
        min_price = prices[0]
        max_price = 0
        # 반복문을 돌려, 최소금액을 구한다(min(현재금액, 최소금액)). 수익 = 현재금액-최소금액
        for i in range(1, len(prices)):
            min_price = min(prices[i], min_price)
            profit = prices[i] - min_price
            max_price = max(profit, max_price)        
        return max_price
    
sol = Solution()
prices = [7,1,5,3,6,4] # 1에 사서 6에 파는 것이 최대수익 
print(sol.max_profit(prices))
