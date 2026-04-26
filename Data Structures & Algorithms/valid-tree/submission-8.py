class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n - 1): 
            return False 
        
        mapping = defaultdict(list)
        
        for parent, child in edges:
            mapping[child].append(parent)
            mapping[parent].append(child) # child -> parent

        visited = set()
        

        def dfs(node):
            if node in visited:
                return 
            
            visited.add(node)
            
            for par in mapping[node]: 
                dfs(par) 

        dfs(0)
        return len(visited) == n
        