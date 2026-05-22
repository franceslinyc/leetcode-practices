#
# @lc app=leetcode id=827 lang=python3
#
# [827] Making A Large Island
#

# @lc code=start
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        # No advantage using BFS 

        # method DFS: O(N^2) time; O(N^2) space

        direction = [[1,0], [-1,0], [0,1], [0,-1]]

        def out_of_bound(r, c):

            return r < 0 or c < 0 or r == N or c == N

        def dfs(r, c, label):

            if out_of_bound(r, c) or grid[r][c] != 1:

                return 0

            grid[r][c] = label   # Mark visited and encode island label so connect() can look it up later

            size = 1             # island size
            
            for dr, dc in direction: 

                size += dfs(r + dr, c + dc, label)            # method 1: LC 200, 695

            # neighbor = [[r+1,c], [r-1,c], [r,c+1], [r,c-1]] # method 2
            
            # for nr, nc in neighbor:
                
            #     size += dfs(nr, nc, label)

            # size += dfs(r+1, c, label)                      # method 3 NO

            # size += dfs(r-1, c, label)

            # size += dfs(r, c+1, label)

            # size += dfs(r, c-1, label)

            return size

        # 1. Precompute island sizes

        N = len(grid)

        label_size_map = defaultdict(int) # Store island label: island size; Default to 0 to avoid KeyError on unseen label  
        
        label = 2  # Use label to label distinct island
                   # Start at 2: 0 reserved for water; 1 reserved for unvisited island 

        for r in range(N):

            for c in range(N):

                if grid[r][c] == 1:

                    label_size_map[label] = dfs(r, c, label) # Have dfs to return total size of the island

                    label += 1

        # At this stage, we'd have a complete map, where its label (keys) start at 2, and label 0 (water) 
        # and 1 (unvisited land) safely return 0 via defaultdict. In addition, the grid now stores labels 
        # for land cells, so given a neighbor's label, we can look up its island size. 

        def connect(r, c): 

            total_size = 1  # the flipped cell itself            

            visited = set() # Prevent double counting of neighbors sharing the same island
                            # Cannot overwrite grid; need original label to look up neighbor

            for dr, dc in direction: 

                nr, nc = r + dr, c + dc
            
            # neighbor = [[r+1,c], [r-1,c], [r,c+1], [r,c-1]]
            
            # for nr, nc in neighbor:

                if not out_of_bound(nr, nc) and grid[nr][nc] not in visited:

                    visited.add(grid[nr][nc])
                    
                    total_size += label_size_map[grid[nr][nc]]  # Sum sizes of all distinct neighboring islands
                    
            return total_size

        # 2. Try flipping water cell

        res = 0 if not label_size_map else max(label_size_map.values()) # Handle the edge case where the grid is all water
                                                                        # Default to the largest existing island if there is no water cell to flip
        for r in range(N):

            for c in range(N):

                if grid[r][c] == 0:

                    res = max(res, connect(r, c))

        return res


# @lc code=end


# e.g., 
# 2 2 0 3    <- flip the 0 at (0,2)
# 2 0 0 3       
# 0 0 0 0

# total_size = 1   # the flipped cell itself at (0,2)
# neighbor (1,2)  (r+1,c) -> label 0 -> label_size_map[0] = 0 (water)        -> total_size = 1
# neighbor (-1,2) (r-1,c) -> out of bounds                                   -> total_size = 1
# neighbor (0,3)  (r,c+1) -> label 3 -> visited={3}, label_size_map[3] = 2   -> total_size = 3
# neighbor (0,1)  (r,c-1) -> label 2 -> visited={2,3}, label_size_map[2] = 3 -> total_size = 6