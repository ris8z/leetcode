import collections
from typing import List

def numIslands(grid: List[List[str]]) -> int:
    visited = set() # (i, j) i is number of row, j is the number of col

    def dfs(row, col):
        if not (0 <= row and row < len(grid)):
            return
        
        if not (0 <= col and col < len(grid[0])):
            return
        
        if grid[row][col] == '0':
            return
        
        if (row, col) in visited:
            return

        visited.add((row, col))

        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    def bfs(row, col):
        queue = collections.deque()
        queue.append((row, col))
        visited.add((row, col))

        while len(queue) > 0:
            r, c = queue.popleft()
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for x,y in directions:
                c_row = r + x
                c_col = c + y
                
                if not(0 <= c_row and c_row < len(grid)) or not(0 <= c_col and c_col < len(grid[0])):
                    continue
                if grid[c_row][c_col] == '0' or (c_row, c_col) in visited:
                    continue
                
                queue.append((c_row, c_col))
                visited.add((c_row, c_col))
    cnt = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '0' or (i, j) in visited:
                continue
            bfs(i, j)
            cnt += 1
    return cnt
