#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])
        island = 0
        visit = set()
        direction = [[1,0], [-1,0], [0,1], [0,-1]]

        def bfs(r, c): 
            q = deque()
            q.append((r, c))  # Starting cell 
            visit.add((r, c)) 
            while q: 
                row, col = q.popleft()
                for dr, dc in direction: 
                    nr = row + dr
                    nc = col + dc
                    if (
                        0 <= nr < rows and 
                        0 <= nc < cols and 
                        grid[nr][nc] == "1" and
                        (nr, nc) not in visit
                    ):
                        q.append((nr, nc))
                        visit.add((nr, nc))

        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == "1" and (r, c) not in visit: 
                    bfs(r, c)   # Explore all connected cells
                    island += 1 # Increment only after exploration of all conneted cells
        return island


# @lc code=end

