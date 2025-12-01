#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # # method 1 dfs

        # direction = [[1,0], [-1,0], [0,1], [0,-1]]
        # rows, cols = len(grid), len(grid[0])
        # island = 0

        # def dfs(r, c): 
        #     if (
        #         0 <= r < rows and
        #         0 <= c < cols and 
        #         grid[r][c] == "1"
        #     ):    
        #         grid[r][c] = "0"
        #         for dr, dc in direction: 
        #             dfs(r + dr, c + dc)
            
        # for r in range(rows): 
        #     for c in range(cols): 
        #         if grid[r][c] == "1": 
        #             dfs(r, c)
        #             island += 1
        # return island

        # method 2 bfs

        direction = [[1,0], [-1,0], [0,1], [0,-1]]
        rows, cols = len(grid), len(grid[0])
        island = 0
        #visit = set()

        def bfs(r, c): 
            q = deque()
            q.append((r, c))  # Starting cell 
            grid[r][c] = "0"  # visit.add((r, c)) 
            
            while q: 
                row, col = q.popleft()
                for dr, dc in direction: 
                    nr = row + dr
                    nc = col + dc
                    if (
                        0 <= nr < rows and 
                        0 <= nc < cols and 
                        grid[nr][nc] == "1" # and
                        # (nr, nc) not in visit
                    ):
                        q.append((nr, nc))
                        grid[nr][nc] = "0" # visit.add((nr, nc))

        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == "1": # if grid[r][c] == "1" and (r, c) not in visit: 
                    bfs(r, c)   # Explore all connected cells
                    island += 1 # Increment only after exploration of all conneted cells
        return island


# @lc code=end

