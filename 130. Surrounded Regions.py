class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        drc = [[0,1],[1,0],[0,-1],[-1,0]]
        visited = set()
        
        def dfs(i, j):
            if i < 0 or i == ROWS or j < 0 or j == COLS or (i,j) in visited or board[i][j] == 'X':
                return
            visited.add((i,j))
            for r, c in drc:
                dfs(i+r, j+c)
        
        for i in range(COLS):
            if board[0][i] == 'O':
                dfs(0, i)
        for i in range(ROWS):
            if board[i][0] == 'O':
                dfs(i, 0)
        for i in range(COLS):
            if board[ROWS-1][i] == 'O':
                dfs(ROWS-1, i)
        for i in range(ROWS):
            if board[i][COLS-1] == 'O':
                dfs(i, COLS-1)

        for i in range(1,ROWS-1):
            for j in range(1, COLS-1):
                if (i,j) not in visited:
                    board[i][j] = 'X'

            
