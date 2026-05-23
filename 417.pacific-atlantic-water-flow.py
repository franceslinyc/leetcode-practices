#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        # method 1: DFS: time O(M*N); space O(M*N)

        ROWS, COLS = len(heights), len(heights[0])

        direction = [[1,0],[-1,0],[0,1],[0,-1]] 

        pacific, atlantic = set(), set()

        def dfs(r, c, visit, prev_height):

            if (r < 0 or c < 0 or r == ROWS or c == COLS or

                (r, c) in visit or

                heights[r][c] < prev_height
            ):

                return

            visit.add((r, c))

            for dr, dc in direction: 

                dfs(r + dr, c + dc, visit, heights[r][c])

            # dfs(r + 1, c, visit, heights[r][c])

            # dfs(r - 1, c, visit, heights[r][c])

            # dfs(r, c + 1, visit, heights[r][c])

            # dfs(r, c - 1, visit, heights[r][c])

        
        # Run DFS from every border cell

        for c in range(COLS):

            dfs(0, c, pacific, heights[0][c])                # Top; Go through cell in first row left to right
                                                             # Start at own height or 0 

            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c]) # Bottom: Go through cell in last row left to right

        for r in range(ROWS):

            dfs(r, 0, pacific, heights[r][0])                # Left; Go through cell in the first col top to bottom

            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1]) # Right; Go thourgh cell in the last col top to bottom 


        # If the cell exists in both sets, add to res
        
        res = []

        for r in range(ROWS):

            for c in range(COLS):

                if (r, c) in pacific and (r, c) in atlantic:

                    res.append([r, c])

        return res


        # method 2: (Multi-source) BFS: time O(M*N); space O(M*N)

        
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