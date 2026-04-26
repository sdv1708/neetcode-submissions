class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = set()

        for a, b in edges:
            # build undirected graph
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node):
            # mark visited, recurse into neighbors
            if node in visited:
                return 

            visited.add(node)

            for nei in adj[node]: 
                dfs(nei)


        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1 

        return count
        