#
# @lc app=leetcode id=827 lang=python3
#
# [827] Making A Large Island
#

# @lc code=start
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        # method DFS: O(N^2) time; O(N^2) space

        N = len(grid)

        def out_of_bound(r, c):

            return r < 0 or c < 0 or r == N or c == N

        def dfs(r, c, label):

            if out_of_bound(r, c) or grid[r][c] != 1:

                return 0

            grid[r][c] = label

            size = 1 

            nei = [[r+1,c], [r-1,c], [r,c+1], [r,c-1]] 
            
            for nr, nc in nei:
                
                size += dfs(nr, nc, label)
            
            return size

        # 1. Precompute island sizes

        label_size_map = defaultdict(int) # Store island label: size; Default to 0 to avoid KeyError on unseen label  
        
        label = 2  # Use label to label distinct island
                   # Start at 2 because 0 reserved for water; 1 reserved for unvisited island 

        for r in range(N):

            for c in range(N):

                if grid[r][c] == 1:

                    label_size_map[label] = dfs(r, c, label) # Have dfs to return total size of the island

                    label += 1

        # At this stage, we'd have a complete map, where keys start at 2, so label 0 (water) and 
        # 1 (unvisited land) safely return 0 via defaultdict

        def connect(r, c):

            visited = set() # Can't modify grid here; labels needed for remaining connect() calls

            res = 1  

            nei = [[r+1,c], [r-1,c], [r,c+1], [r,c-1]]
            
            for nr, nc in nei:

                if not out_of_bound(nr, nc) and grid[nr][nc] not in visited:

                    visited.add(grid[nr][nc])
                    
                    res += label_size_map[grid[nr][nc]] 
                    
            return res

        # 2. Try flipping water cell

        res = 0 if not label_size_map else max(label_size_map.values()) # Handle the edge case where the grid is all water
                                                                        # Default to the largest existing island if there is no water cell to flip
        for r in range(N):

            for c in range(N):

                if grid[r][c] == 0:

                    res = max(res, connect(r, c))

        return res


# @lc code=end

