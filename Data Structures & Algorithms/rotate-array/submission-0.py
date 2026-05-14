class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n # normalizing the k so that it always stays in range

        def rev(l , r):
            while l < r: 
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1 
        
        
        # reverse the entire array 
        rev(0, n - 1)
        # reverse the first k elements after step 1 
        rev(0, k - 1)
        # reverse the last k elements after step 2 
        rev(k, n - 1)

            


        