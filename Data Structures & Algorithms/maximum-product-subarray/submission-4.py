class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = currMin = result = nums[0]

        for i in range(1, len(nums)):
            tempMax = currMax 
            currMax = max(currMax * nums[i], currMin * nums[i], nums[i])
            currMin = min(tempMax * nums[i], currMin * nums[i], nums[i])
            result = max(result, currMax)
        
        return result



        