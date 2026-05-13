class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1) 
        len2 = len(word2)
        
        l, r = 0, 0 
        res = []

        while l < len1 or r < len2:
            if l < len1: 
                res.append(word1[l])
            if r < len2: 
                res.append(word2[r])
            
            l += 1 
            r += 1 
        
        return "".join(res)



        