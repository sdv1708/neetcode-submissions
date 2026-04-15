class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        result = []

        def backtrack(start_index, current_sum, path): 

            if current_sum == target: 
                result.append(list(path))
                return 
            
            if current_sum > target: 
                return 
            
            for i in range(start_index, len(nums)): 
                if i > start_index and nums[i] == nums[i-1]: 
                    continue 
                path.append(nums[i])
                backtrack(i+1, current_sum + nums[i], path)
                path.pop()
        
        backtrack(0, 0, [])
        return result

