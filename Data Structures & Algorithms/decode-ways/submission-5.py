class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': 
            return 0 
        
        n = len(s)
        dp = [0] * n

        dp[0] = 1 

        for i in range(1, n):
            one = s[i] # current character
            two = s[i-1:i+1] # prev + current 

            if '1' <= one <= '9': 
                dp[i] += dp[i-1]
            
            if i >= 2 and '10' <= two <= '26': 
                dp[i] += dp[i-2]
            elif i == 1 and '10' <= two <= '26':
                dp[i] += 1
        
        return dp[n-1]