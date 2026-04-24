class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        island = 0 

        def dfs(r, c): 
            if r >= rows or c >= cols or r < 0 or c < 0 or grid[r][c] == '0':
                return 

            grid[r][c] = '0' # mark as visited 
            for dr, dc in dirs: 
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols): 
                if grid[r][c] == '1': 
                    dfs(r, c)
                    island += 1 

        return island 

