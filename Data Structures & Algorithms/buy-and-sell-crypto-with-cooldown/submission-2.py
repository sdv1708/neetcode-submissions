class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        # Three states to be tracked
        holding = [0] * n  # Max profit with a stock in hand
        sold = [0] * n     # Max profit at end of day, having sold on this day
        cooldown = [0] * n # Max profit at end of day, currently in cooldown
        
        # Base case
        holding[0] = -prices[0]
        
        for i in range(1, n):
            # To hold, we either kept the stock or bought after a cooldown
            holding[i] = max(holding[i-1], cooldown[i-1] - prices[i])
            # To sell, we must have been holding the stock
            sold[i] = holding[i - 1] + prices[i]
            # To be in cooldown, we must have sold the day before
            cooldown[i] = max(cooldown[i-1], sold[i-1])
            
        return max(sold[-1], cooldown[-1])
