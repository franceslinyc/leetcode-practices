#
# @lc app=leetcode id=286 lang=python3
#
# [286] Walls and Gates
#

# @lc code=start
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        # method 1: BFS: time O((M*N)^2); space O(M*N)

        # # method 2: Multi Source BFS, Distance Propagation: time O(M*N); space O(M*N)

        # ROWS, COLS = len(rooms), len(rooms[0])

        # directions = [[1,0], [-1,0], [0,1], [0,-1]]

        # INF = 2147483647

        # # Put all gates in the queue

        # q = deque()

        # for r in range(ROWS):

        #     for c in range(COLS):

        #         if rooms[r][c] == 0:

        #             q.append((r, c))

        # # Run BFS from all gates

        # while q:

        #     row, col = q.popleft()

        #     for dr, dc in directions:

        #         nr, nc = row + dr, col + dc

        #         if (0 <= nr < ROWS and

        #             0 <= nc < COLS and

        #             rooms[nr][nc] == INF):

        #             rooms[nr][nc] = rooms[row][col] + 1  # Distance propagation
        #                                                  # Initially rooms[row][col] = 0 because it is a gate! 

        #             q.append((nr, nc))


        # method 2: Multi Source BFS, Level BFS: time O(M*N); space O(M*N) 

        ROWS, COLS = len(rooms), len(rooms[0])

        direction = [[1,0], [-1,0], [0,1], [0,-1]]

        INF = 2147483647

        #visit = set() # Use it if grid cannot be modified 

        # Put all gates in the queue

        q = deque()

        for r in range(ROWS):

            for c in range(COLS):

                if rooms[r][c] == 0:

                    q.append([r, c])

                    #visit.add((r, c))

        # Run BFS from all gates

        distance = 0

        while q:                          # Process all levels 

            distance += 1

            for i in range(len(q)):       # Process ALL nodes in the current level

                row, col = q.popleft()

                #rooms[row][col] = dist

                for dr, dc in direction: 

                    nr, nc = row + dr, col + dc

                    if (0 <= nr < ROWS and 
                    
                        0 <= nc < COLS and 

                        rooms[nr][nc] == INF     # rooms[nr][nc] == INF already mean unvisited! 

                        #rooms[nr][nc] != -1 and 

                        #(nr, nc) not in visit
                    ): 
                        
                        rooms[nr][nc] = distance

                        q.append((nr, nc))

                        #visit.add((nr, nc))


        # method 3: DFS or Backtracking but is slow because this approach reexplores the same areas again and again


# Multi-source BFS, Distance Propagation:
#
# Start BFS from all source nodes (i.e., all gates with value 0) at the same time. 
#
# Multi-source BFS, Level BFS:
#
# Process the queue layer by layer, where each layer represents nodes at the same distance from 
# the source node. 


# @lc code=end

