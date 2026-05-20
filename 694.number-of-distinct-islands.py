#
# @lc app=leetcode id=694 lang=python3
#
# [694] Number of Distinct Islands
#

# @lc code=start
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        def dfs(r, c):

            if r < 0 or c < 0 or r >= ROWS or c >= COLS:

                return

            if grid[r][c] == 0 or (r, c) in seen:

                return

            seen.add((r, c))

            # Instead of storing the absolute position, store the position RELATIVE to the island's starting cell (r0, c0).

            current_island.add((r - r0, c - c0))    # Store this cell as normalized coordinate relative to island's top-left start

            # Explore all 4 directions

            dfs(r + 1, c)

            dfs(r - 1, c)

            dfs(r, c + 1)

            dfs(r, c - 1)

            # nei = [[r+1,c], [r-1,c], [r,c+1], [r,c-1]] 
            
            # for nr, nc in nei:    

            #     dfs(nr, nc)     

        ROWS, COLS = len(grid), len(grid[0])

        seen = set()

        unique_islands = set()

        for r in range(ROWS):

            for c in range(COLS):

                r0, c0 = r, c          # Use the first discovered land cell of this island as the reference point for normalization. 
                                       # Every other land cell in the island will be stored to this starting point. 

                current_island = set() # Store normalized coordinates of every land cells in this island

                dfs(r, c)

                if current_island:     # Only add if an island was found; Skip water cells 

                    unique_islands.add(frozenset(current_island))

        return len(unique_islands)        


# current_island
# -> temporary working (mutable) set while DFS is building shape
# frozenset(current_island)
# -> finalized immutable “signature” of that island
# unique_islands
# -> collection of unique signatures only


# e.g., 
# grid 
# 1 1 0 0
# 1 0 0 0
# 0 0 1 1
# 0 0 1 0

# Island A raw cells:    Island B raw cells:
# (0,0)                  (2,2)
# (0,1)                  (2,3)
# (1,0)                  (3,2)

# Island A starts at (0, 0) so every cell in Island A subtracts (0, 0)
# Island B starts at (2, 2) so every cell in Island B subtracts (2, 2)

# Island A offsets:      Island B offsets:
# (0-0, 0-0) = (0,0)    (2-2, 2-2) = (0,0)
# (0-0, 1-0) = (0,1)    (2-2, 3-2) = (0,1)
# (1-0, 0-0) = (1,0)    (3-2, 2-2) = (1,0)

# current_island A = {(0,0), (0,1), (1,0)}
# current_island B = {(0,0), (0,1), (1,0)}  <- Identical!

# unique_islands.add(frozenset({(0,0), (0,1), (1,0)}))  <- Island A added
# unique_islands.add(frozenset({(0,0), (0,1), (1,0)}))  <- Island B silently ignored, duplicate
# unique_islands = {frozenset({(0,0), (0,1), (1,0)}) =}
# len(unique_islands) = 1


# @lc code=end

