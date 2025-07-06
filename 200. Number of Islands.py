class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        visited = [[False for c in range(COLS)] for r in range(ROWS)]
        
        
        def dfs(r,c):
            if r < 0 or r > ROWS-1 or c < 0 or c > COLS -1 or visited[r][c] or grid[r][c] == '0':
                return
            visited[r][c] = True
            for drc in directions:
                dfs(r+drc[0], c+drc[1])

        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if not visited[r][c] and grid[r][c] == '1':
                    islands += 1
                    dfs(r,c)
        return islands

            
                    


        