class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_map = defaultdict(list)
        for cou, pre in prerequisites:  
            adj_map[cou].append(pre) # course -> prereq mapping 

        visited = set()

        def dfs(course, visiting):  
            if course in visiting: 
                return False    
            
            if course in visited: 
                return True
            
            visiting.add(course)

            for pre in adj_map[course]: 
                if not dfs(pre, visiting): 
                    return False 
            visited.add(course)
            visiting.remove(course)
            return True

        visiting = set()
        for cou, pre in prerequisites:
            if not dfs(cou, visiting): 
                return False 

        return True 


            
            



        