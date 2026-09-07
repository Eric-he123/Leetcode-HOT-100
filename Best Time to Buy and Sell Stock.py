# 只需维护min_price和max_profit两个变量即可，每到下一天都检查当前卖出的话利润是多少，由于每一次都会维护min_price，所以当前价格的profit总是会与min_price对比

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            profit = prices[i] - min_price
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, profit)
        return max_profit
