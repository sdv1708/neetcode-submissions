class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        # If the string is empty, there are no valid decodings
        if n == 0:
            return 0

        # A message cannot start with '0'
        if s[0] == '0':
            return 0

        # dp[i] = number of ways to decode the first i characters
        # So dp[0] = ways to decode empty prefix
        dp = [0] * (n + 1)

        # Empty prefix has 1 way: do nothing
        dp[0] = 1

        # First character is guaranteed non-zero here, so it has 1 decoding
        dp[1] = 1

        # Build the answer for prefixes of length 2 to n
        for i in range(2, n + 1):
            # Last one digit of the current prefix s[0:i] 
            one = s[i - 1:i] # up until right before i, basically same as s[i-1]

            # Last two digits of the current prefix s[0:i]
            two = s[i - 2:i]

            # Case 1: decode the last one digit alone
            # Valid only if it is between '1' and '9'
            if '1' <= one <= '9':
                dp[i] += dp[i - 1]

            # Case 2: decode the last two digits together
            # Valid only if it is between "10" and "26"
            if '10' <= two <= '26':
                dp[i] += dp[i - 2]

        # dp[n] = number of ways to decode the whole string
        return dp[n]