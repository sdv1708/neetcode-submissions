class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
            
        holding = [0] * n 
        sold = [0] * n
        cooldown = [0] * n
        
        holding[0] = -prices[0] # you have to buy on the first day
        
        # sold[0] and cooldown[0] are already 0
        
        for i in range(1, n):
            # You either keep holding or buy after a rest period
            holding[i] = max(holding[i-1], cooldown[i-1] - prices[i])
            # You must have held the stock to sell it
            sold[i] = holding[i-1] + prices[i]
            # You either rest after selling or continue resting
            cooldown[i] = max(cooldown[i-1], sold[i-1])
            
        return max(sold[-1], cooldown[-1])
