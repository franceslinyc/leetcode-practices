#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        # # method 1: DFS: time O(M*N); space O(M*N)

        # ROWS, COLS = len(heights), len(heights[0])

        # direction = [[1,0],[-1,0],[0,1],[0,-1]] 

        # pacific, atlantic = set(), set()

        # def dfs(r, c, visit, prev_height):

        #     if (r < 0 or c < 0 or r == ROWS or c == COLS or

        #         (r, c) in visit or

        #         heights[r][c] < prev_height # May go to neighor only if heights[nr][nc] >= heights[r][c]
        #     ):

        #         return

        #     visit.add((r, c))

        #     for dr, dc in direction: 

        #         dfs(r + dr, c + dc, visit, heights[r][c])

        #     # dfs(r + 1, c, visit, heights[r][c])

        #     # dfs(r - 1, c, visit, heights[r][c])

        #     # dfs(r, c + 1, visit, heights[r][c])

        #     # dfs(r, c - 1, visit, heights[r][c])

        
        # # Run DFS from every border cell

        # for c in range(COLS):

        #     dfs(0, c, pacific, heights[0][c])                # Top; Go through cell in first row left to right
        #                                                      # Start at own height or 0 

        #     dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c]) # Bottom: Go through cell in last row left to right

        # for r in range(ROWS):

        #     dfs(r, 0, pacific, heights[r][0])                # Left; Go through cell in the first col top to bottom

        #     dfs(r, COLS - 1, atlantic, heights[r][COLS - 1]) # Right; Go thourgh cell in the last col top to bottom 


        # # If the cell exists in both sets, add to res
        
        # res = []

        # for r in range(ROWS):

        #     for c in range(COLS):

        #         if (r, c) in pacific and (r, c) in atlantic:

        #             res.append([r, c])

        # return res


        # method 2: (Multi-source) BFS: time O(M*N); space O(M*N)

        ROWS, COLS = len(heights), len(heights[0])

        direction = [[1,0],[-1,0],[0,1],[0,-1]] 


        # 1. Create two boolean grids
        # Use two to track these two conditions independently 

        pac = [[False] * COLS for _ in range(ROWS)]

        atl = [[False] * COLS for _ in range(ROWS)]  


        # 2. Build two source lists
        # q_pac: all cells on top row + left column 
        # q_atl: all cells on bottom row + right column 
        
        q_pac = [] 

        q_atl = []

        for c in range(COLS):

            q_pac.append((0, c))        # top row

            q_atl.append((ROWS - 1, c)) # bottom row

        for r in range(ROWS):

            q_pac.append((r, 0))        # left col

            q_atl.append((r, COLS - 1)) # right col


        # 3. Write BFS

        def bfs(source, ocean):  # source, instead of r, c, because we'd need to call list of cells, instead of one cell

            for r, c in source:               # source marking

                ocean[r][c] = True            # Same role as grid[r][c] = "0" in LC 200 but apply to 
                                              # every source cell instead of one cell

            q = deque(source)

            while q:

                row, col = q.popleft()

                #ocean[row][col] = True

                for dr, dc in direction:

                    nr, nc = row + dr, col + dc

                    if (0 <= nr < ROWS and 
                        
                        0 <= nc < COLS and
                        
                        not ocean[nr][nc] and # Hasn't been visited 

                        heights[nr][nc] >= heights[row][col] 
                    ):
                        
                        ocean[nr][nc] = True  # neighbor marking 

                        q.append((nr, nc))


        # 3. Run BFS for pacific source list (q_pac) and atlantic source list (q_atl)
        # all of those cells go into the queue at once, and BFS expands outward (uphill) from all of them simultaneously, marking everything reachable as True in the pac grid.

        bfs(q_pac, pac)

        bfs(q_atl, atl)

        
        # 4. Collect res
        
        res = []

        for r in range(ROWS):

            for c in range(COLS):

                if pac[r][c] and atl[r][c]:

                    res.append([r, c])

        return res

        
# @lc code=end


# e.g., 
#              Pacific
#              ↓↓↓↓↓
# Pacific → [1, 2, 2, 3, 5]
# Pacific → [3, 2, 3, 4, 4]
# Pacific → [2, 4, 5, 3, 1]
# Pacific → [6, 7, 1, 4, 5]
# Pacific → [5, 1, 1, 2, 4] ← Atlantic
#              ↑↑↑↑↑
#              Atlantic

# First for loop (c from 0,1,2,3):

#   Pacific:
#   dfs(0,0), dfs(0,1), dfs(0,2), dfs(0,3)   ← top row
#   Atlantic:
#   dfs(3,0), dfs(3,1), dfs(3,2), dfs(3,3)   ← bottom row

# Second for loop (r from 0,1,2,3):

#   Pacific:
#   dfs(0,0), dfs(1,0), dfs(2,0), dfs(3,0)   ← left col  Note that (0,0) already in visit (pacific) 
#   Atlantic:
#   dfs(0,3), dfs(1,3), dfs(2,3), dfs(3,3)   ← right col Note that (3,3) already in visit (atlantic)