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

        # island = 0

        # def dfs(r, c): 

        #     if (
        #         0 <= r < ROWS and

        #         0 <= c < COLS and 
                
        #         grid[r][c] == "1"
        #     ):    
                
        #         grid[r][c] = "0"
                
        #         for dr, dc in direction: 
                    
        #             dfs(r + dr, c + dc)

        # ROWS, COLS = len(grid), len(grid[0])

        # for r in range(ROWS): 

        #     for c in range(COLS): 

        #         if grid[r][c] == "1": 

        #             dfs(r, c)

        #             island += 1

        # return island


        # method 2 bfs

        direction = [[1,0], [-1,0], [0,1], [0,-1]]

        island = 0

        #visit = set() # Can ignore; Alternative way

        # BFS function to explore an entire island

        def bfs(r, c): 

            # Mark the starting land cell as visited 

            grid[r][c] = "0"  # visit.add((r, c)) 

            q = deque()

            q.append((r, c))  # Starting cell 
   
            while q: 

                row, col = q.popleft()   # Process node one-by-one, VS LC 102

                # Check all 4 possible directions

                for dr, dc in direction: 

                    nr = row + dr # nr: new row 

                    nc = col + dc # nc: new col

                    if (
                        0 <= nr < ROWS and 

                        0 <= nc < COLS and 
                        
                        grid[nr][nc] == "1" # and
                        # (nr, nc) not in visit
                    ):
                        
                        grid[nr][nc] = "0" # visit.add((nr, nc))

                        q.append((nr, nc)) 

        # Traverse every cell in the grid

        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS): 

            for c in range(COLS): 

                # If we find unvisited land, 

                if grid[r][c] == "1": # if grid[r][c] == "1" and (r, c) not in visit: 
                    
                    bfs(r, c)   # Explore all connected cells
                    
                    island += 1 # Increment only after exploration of all conneted cells
        
        return island


# Ques: 
# 1. Grid is non-empty?
# 2. Cells are only "0" or "1"? 
# 3. We only search/connect left/right/up/down?
# 4. Can we modify the grid? 
# 
# BFS: 
# 
# DFS: 
# 
# We treat each land cell as a node in a graph. We iterate through the grid, and whenever we find 
# an unvisited land cell, we increment the island count and perform a DFS or BFS to mark the 
# entire connected component as visited. Since each cell is processed once, the time complexity is 
# O(m x n), and space complexity is O(m x n).


# @lc code=end

