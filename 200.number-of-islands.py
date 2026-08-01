#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # No advantage using BFS 
        
        # # method 1 DFS: time O(M*N); space O(M*N)

        # direction = [[1,0], [-1,0], [0,1], [0,-1]]

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

        # island = 0

        # for r in range(ROWS): 

        #     for c in range(COLS): 

        #         if grid[r][c] == "1": 

        #             dfs(r, c)

        #             island += 1

        # return island


        # method 2 BFS: time O(M*N); space O(M*N)

        direction = [[1,0], [-1,0], [0,1], [0,-1]]

        # BFS function to explore an entire island

        def bfs(r, c): 

            # Better let BFS do one thing: flood-fill and mark visited, nothing else. Else, 
            # need to return OUTSIDE of while loop like LC 695 does. 

            # Mark the starting land cell as visited 

            grid[r][c] = "0"  

            q = deque()

            q.append((r, c))  

            # Use both deque() + .append OR deque([(r, c)]) 
   
            while q: 

                row, col = q.popleft()   # Process node one-by-one, VS LC 102

                # Check all 4 possible directions

                for dr, dc in direction: 

                    nr = row + dr # nr: new row 

                    nc = col + dc # nc: new col

                    if (0 <= nr < ROWS and 

                        0 <= nc < COLS and 
                        
                        grid[nr][nc] == "1" 
                    ):
                        
                        grid[nr][nc] = "0" 

                        q.append((nr, nc)) 

        # Traverse every cell in the grid

        ROWS, COLS = len(grid), len(grid[0])
    
        island = 0

        for r in range(ROWS): 

            for c in range(COLS): 

                # If we find unvisited land, 

                if grid[r][c] == "1": 
                    
                    bfs(r, c)   # Explore all connected cells
                    
                    island += 1 # Increment only after exploration of all conneted cells
        
        return island


# @lc code=end


# e.g., 
# Input: grid = [
#   ["1","1","0","0","0"], 
#   ["1","1","0","0","0"], 
#   ["0","0","1","0","0"], 
#   ["0","0","0","1","1"]
# ]
# Output: 3 

# 1 at (0,0) -> add (0,1), (1,0)
# 1 at (0,1) -> add (1,1)
# 1 at (1,0) -> (1,1) already marked, nothing new
# 1 at (1,1) -> all neighbors 0, nothing new
# island 1 done

# 1 at (2,2) -> all neighbors 0, nothing new
# island 2 done

# 1 at (3,3) -> add (3,4)
# 1 at (3,4) -> all neighbors 0, nothing new
# island 3 done

# Start at (0,0) 
# BFS all neighbors
#     add neighbors' neighbors to q
# BFS neighbors' neighbors but it's 0 

# We treat each land cell as a node in a graph. We iterate through the grid, and whenever we find 
# an unvisited land cell, we increment the island count and perform a DFS or BFS to mark the 
# entire connected component as visited. Since each cell is processed once, the time complexity is 
# O(m x n), and space complexity is O(m x n).

