class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        
        pac = set() # tracking grids which touch the pacfic ocean 
        atl = set()
     
        dirs =  [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, visited):
            if (r, c) not in visited:
                visited.add((r, c))

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc 

                if nr not in range(ROWS) or nc not in range(COLS):
                    continue 

                if (nr, nc) in visited:
                    continue 

                if heights[nr][nc] < heights[r][c]: 
                    continue 

                dfs(nr, nc, visited) 

        # pacific top row 
        for c in range(COLS): 
            if (0, c) not in pac:
                dfs(0, c, pac)

        # pacific first col
        for r in range(ROWS): 
            if (r, 0) not in pac:
                dfs(r, 0, pac)
        
        # atlantic last col  
        for r in range(ROWS): 
            if (r, COLS - 1) not in atl:
                dfs(r, COLS - 1, atl)
        
        # atlantic bottom row
        for c in range(COLS): 
            if (ROWS - 1, c) not in atl:
                dfs(ROWS - 1, c, atl)
        
        result = []
        for r in range(ROWS): 
            for c in range(COLS): 
                if (r, c) in pac and (r, c) in atl: 
                    result.append([r, c])
        
        return result

        