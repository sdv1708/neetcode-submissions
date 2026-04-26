class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_map = defaultdict(list)
        for cou, pre in prerequisites:  
            adj_map[cou].append(pre) # course -> prereq mapping 
        
        result = []

        visited = set()
        cycle = set()
        def dfs(course): 
            if course in cycle:
                return False 

            if course in visited: 
                return True 

            cycle.add(course)

            for pre in adj_map[course]: 
                if not dfs(pre): 
                    return False 

            cycle.remove(course)
            visited.add(course)
            result.append(course)

            return True 

        for course in range(numCourses): 
            if not dfs(course):
                return []
        
        return result



        