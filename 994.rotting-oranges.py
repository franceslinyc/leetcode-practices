#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # method 1: Multi-source BFS, Level BFS: time O(M*N); space O(M*N)
        
        ROWS, COLS = len(grid), len(grid[0])

        direction = [[1,0],[-1,0],[0,1],[0,-1]]

        q = deque()

        fresh = 0    # Count the #s of fresh oranges             

        for r in range(ROWS): 

            for c in range(COLS): 

                if grid[r][c] == 2: 

                    q.append((r, c))

                if grid[r][c] == 1: 

                    fresh += 1

        time = 0 

        while q and fresh > 0: # while q: 

            time += 1

            for i in range(len(q)):        # Process the current level 

                row, col = q.popleft()
                
                for dr, dc in direction: 

                    nr, nc = row + dr, col + dc 

                    if (0 <= nr < ROWS and 

                        0 <= nc < COLS and 

                        grid[nr][nc] == 1   # If this is fresh orange

                    ): 

                        grid[nr][nc] = 2   # Mark as rotten 

                        q.append((nr, nc))

                        fresh -= 1

        return time if fresh == 0 else -1 


# Refer to LC 286's notes        


# @lc code=end

