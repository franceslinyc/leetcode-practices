#
# @lc app=leetcode id=317 lang=python3
#
# [317] Shortest Distance from All Buildings
#

# @lc code=start
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])

        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        
        # Store total distance from this empty land to all buildings 
        dist_matrix = [[0] * COLS for _ in range(ROWS)]

        empty_land = 0
        building = 1
        obstacle = 2

        min_dist = float('inf')

        def bfs(r, c):

            q = deque()

            q.append((r, c, 0))

            # Store distance from current building 
            local_dist = float('inf')

            while q: # Every reachable cell (empty land) from this building 

                row, col, dist = q.popleft()

                for dr, dc in directions:

                    nr, nc = row + dr, col + dc

                    if (0 <= nr < ROWS and

                        0 <= nc < COLS and

                        grid[nr][nc] == empty_land):

                        # Mark visited for this building
                        grid[nr][nc] -= 1 # Control repeated visit by different building

                        # Increment distance for this building 
                        dist_matrix[nr][nc] += dist + 1

                        q.append((nr, nc, dist + 1))

                        local_dist = min(local_dist, dist_matrix[nr][nc])

            return local_dist

        # Run bfs for all buildings
        for r in range(ROWS):

            for c in range(COLS):

                if grid[r][c] == building:

                    local_dist = bfs(r, c)

                    empty_land -= 1      # Control repeated visit by different building
                    
                    min_dist = local_dist

        return min_dist if min_dist != float('inf') else -1
     
           
# @lc code=end

