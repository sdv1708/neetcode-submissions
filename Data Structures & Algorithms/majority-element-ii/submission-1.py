class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums: 
            freq[num] = 1 + freq.get(num, 0)
        
        k = len(nums) // 3 
        res = []
        for key in freq: 
            if freq[key] > k: 
                res.append(key)
        
        return res

        