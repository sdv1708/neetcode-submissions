class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        INF = float('inf')
        dp = [INF] * (amount + 1)

        dp[0] = 0 

        for amt in range(1, amount + 1): 
            for c in coins: 
                if (amt - c) >= 0 and dp[amt-c] != INF: 
                    dp[amt] = min(dp[amt], dp[amt-c] + 1)
        
        return dp[amount] if dp[amount] != INF else -1

        