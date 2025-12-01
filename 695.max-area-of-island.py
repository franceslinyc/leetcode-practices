#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # # method 1 dfs

        # #direction = [[1,0], [-1,0], [0,1], [0,-1]]
        # rows, cols = len(grid), len(grid[0])
        # area = 0
        # visit = set()

        # def dfs(r, c): 
        #     if (
        #         r < 0 or r == rows or 
        #         c < 0 or c == cols or 
        #         grid[r][c] == 0 or
        #         (r, c) in visit
        #     ):
        #         return 0 
        #     visit.add((r, c))
        #     return (1 + dfs(r + 1, c) +
        #                 dfs(r - 1, c) +
        #                 dfs(r, c + 1) +
        #                 dfs(r, c - 1))

        # for r in range(rows): 
        #     for c in range(cols): 
        #         if grid[r][c] == 1 and (r, c) not in visit: # Redundant
        #             area = max(area, dfs(r, c))
        # return area

        # method 2 bfs

        direction = [[1,0], [-1,0], [0,1], [0,-1]]
        rows, cols = len(grid), len(grid[0])
        area = 0

        def bfs(r, c): 
            q = deque()
            q.append((r, c))
            grid[r][c] = 0                  # int, not str, so not "0"
            res = 1
            
            while q: 
                row, col = q.popleft()
                for dr, dc in direction: 
                    nr = row + dr
                    nc = col + dc
                    if (
                        0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc] == 1   # int, not str, so not "0"
                        ):
                        q.append((nr, nc))
                        grid[nr][nc] = 0
                        res += 1
            return res 

        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == 1:         # int, not str, so not "0"
                    area = max(area, bfs(r, c))
        return area

        
# @lc code=end

