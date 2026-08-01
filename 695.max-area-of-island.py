#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # No advantage using BFS 

        # # method 1 DFS: time O(M*N); space O(M*N)

        # direction = [[1,0], [-1,0], [0,1], [0,-1]]

        # def dfs(r, c): 

        #     if not (
        #         0 <= r < ROWS and

        #         0 <= c < COLS and 

        #         grid[r][c] == 1
        #     ):    
        #         return 0

        #     grid[r][c] = 0
            
        #     area = 1 
            
        #     for dr, dc in direction: 
                
        #         area += dfs(r + dr, c + dc)
                
        #     return area

        # ROWS, COLS = len(grid), len(grid[0])

        # max_area = 0

        # for r in range(ROWS): 

        #     for c in range(COLS): 

        #         if grid[r][c] == 1:

        #             area = dfs(r, c)
                    
        #             max_area = max(max_area, area)

        # return max_area


        # method 2 BFS: time O(M*N); space O(M*N)

        direction = [[1,0], [-1,0], [0,1], [0,-1]]

        def bfs(r, c): 

            grid[r][c] = 0 

            q = deque()

            q.append((r, c))

            # Use both deque() + .append OR deque([(r, c)]) 

            area = 1   

            while q: 

                row, col = q.popleft()

                for dr, dc in direction: 

                    nr, nc = row + dr, col + dc

                    if (0 <= nr < ROWS and

                        0 <= nc < COLS and

                        grid[nr][nc] == 1
                    ):

                        grid[nr][nc] = 0

                        q.append((nr, nc))

                        area += 1

            return area

        ROWS, COLS = len(grid), len(grid[0])

        max_area = 0

        for r in range(ROWS): 

            for c in range(COLS): 

                if grid[r][c] == 1:
                    
                    area = bfs(r, c)        # Return "local" area
                    
                    max_area = max(max_area, area)
                    
        return max_area


# @lc code=end


# Refer to LC 200's notes
