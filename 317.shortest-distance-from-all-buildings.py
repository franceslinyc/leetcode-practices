#
# @lc app=leetcode id=317 lang=python3
#
# [317] Shortest Distance from All Buildings
#

# @lc code=start
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:

        # method 1 bfs: time O(B * M * N), where B = # of building, O((M*N) * M * N = O(M^2 * N^2) worst case; space O(M * N)
        
        ROWS, COLS = len(grid), len(grid[0])

        direction = [[1,0], [-1,0], [0,1], [0,-1]]       # Can use tuple too, i.e., [(1,0),(-1,0),(0,1),(0,-1)]

        dist_matrix = [[0] * COLS for _ in range(ROWS)]  # Store total distance from this empty land to all buildings 

        min_dist = float('inf')

        empty_land = 0

        building = 1

        def bfs(r, c): 

            local_dist = float('inf')  # Track minimum cumulative distance among valid cells so far

            q = deque()

            q.append((r, c, 0))

            while q:  # Go through empty lands reachable from this building

                row, col, dist = q.popleft()

                for dr, dc in direction:

                    nr, nc = row + dr, col + dc

                    if (0 <= nr < ROWS and

                        0 <= nc < COLS and

                        grid[nr][nc] == empty_land):

                        grid[nr][nc] -= 1               # Ensure each BFS only visits cells reachable by all previous buildings; Differ from LC 200 & 695; 

                        dist_matrix[nr][nc] += dist + 1 # Increment distance for this building

                        q.append((nr, nc, dist + 1)) 

                        local_dist = min(local_dist, dist_matrix[nr][nc]) # Tricky! 

            return local_dist
            
        # Run bfs for all buildings

        for r in range(ROWS):

            for c in range(COLS):

                if grid[r][c] == building:

                    local_dist = bfs(r, c)  

                    min_dist = local_dist   # Since local_dist already represents the minimum cumulative distance

                    empty_land -= 1         # Control repeated visit by different building

        return min_dist if min_dist != float('inf') else -1

        
        # ROWS, COLS = len(grid), len(grid[0])

        # directions = [(-1,0),(1,0),(0,1),(0,-1)]

        # dist_matrix = [[0] * COLS for _ in range(ROWS)]

        # empty_land = 0

        # building = 1

        # min_dist = float('inf')

        # for r in range(ROWS):

        #     for c in range(COLS):
                
        #         if grid[r][c] == building:

        #             local_dist = float('inf') 

        #             q = deque()

        #             q.append((r, c, 0))

        #             while q:

        #                 row, col, dist = q.popleft()

        #                 for dr, dc in directions:

        #                     nr, nc = row + dr, col + dc

        #                     if (0 <= nr < ROWS and

        #                         0 <= nc < COLS and

        #                         grid[nr][nc] == empty_land):

        #                         grid[nr][nc] -= 1

        #                         dist_matrix[nr][nc] += dist + 1

        #                         q.append((nr, nc, dist + 1))

        #                         local_dist = min(local_dist, dist_matrix[nr][nc])
                    
        #             empty_land -= 1

        #             min_dist = local_dist

        # return min_dist if min_dist != float('inf') else -1


# Related to LC 200 and 695


# @lc code=end

