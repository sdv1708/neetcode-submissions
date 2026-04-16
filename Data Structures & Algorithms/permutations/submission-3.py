class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []

        def backtrack(visited, path): 
            if len(path) == len(nums): 
                result.append(list(path))
                return

            for i in range(len(nums)): 
                if nums[i] in visited: 
                    continue 
                path.append(nums[i])
                visited.add(nums[i])

                backtrack(visited, path)
                path.pop()
                visited.remove(nums[i])
        
        visited = set()
        backtrack(visited, [])
        return result
  

        

        