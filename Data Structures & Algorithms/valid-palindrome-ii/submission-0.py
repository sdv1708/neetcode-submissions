class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True 
        
        l, r = 0, len(s) - 1
        while l < r: 
            if s[l] != s[r]: 
                # Be careful about the exclusivity of th ending index !!
                skipLeft = s[l + 1 : r + 1] # if skipping left character 
                skipRight = s[l : r] # if skipping right character 
                return skipLeft == skipLeft[::-1] or skipRight == skipRight[::-1]
            
            l += 1 
            r -= 1
        
        return True
                
            
        