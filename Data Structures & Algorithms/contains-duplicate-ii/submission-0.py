class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = r = 0 

        dupl = set()

        while r < len(nums): 
            if nums[r] in dupl:
                return True 
            dupl.add(nums[r])

            if (r - l) >= k: 
                dupl.remove(nums[l])
                l += 1

            r += 1 

        return False 
