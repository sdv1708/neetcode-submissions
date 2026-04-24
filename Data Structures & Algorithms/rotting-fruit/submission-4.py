class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        fresh = 0
        time = 0 
        queue = deque()

        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for r in range(ROWS): 
            for c in range(COLS): 
                if grid[r][c] == 1:
                    fresh += 1 
                if grid[r][c] == 2: 
                    queue.append((r, c))

        while queue and fresh > 0: 
            for _ in range(len(queue)) :
                r, c = queue.popleft()

                for dr, dc in dirs: 
                    nr, nc = r + dr, c + dc 

                    if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 1: 
                        grid[nr][nc] = 2 
                        fresh -= 1 
                        queue.append((nr, nc))
                    
            time += 1 

        if fresh != 0: 
            return -1 
        return time





                



        
            
