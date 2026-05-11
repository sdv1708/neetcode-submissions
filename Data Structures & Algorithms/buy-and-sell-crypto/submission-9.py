class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 
        minBuy = prices[0] 

        for i in range(len(prices)): 
            minBuy = min(minBuy, prices[i])
            profit = prices[i] - minBuy 
            maxProfit = max(maxProfit, profit)

        return maxProfit 
        