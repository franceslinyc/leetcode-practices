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

        # method 2: Multi Source BFS: time O(M*N); space O(M*N)

        ROWS, COLS = len(rooms), len(rooms[0])

        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        #visit = set()

        INF = 2147483647

        # Put all gates in the queue

        q = deque()

        for r in range(ROWS):

            for c in range(COLS):

                if rooms[r][c] == 0:

                    q.append((r, c))

                    # visit.add((r, c))

        # Run BFS from all gates

        while q:

            row, col = q.popleft()

            for dr, dc in directions:

                nr, nc = row + dr, col + dc

                if (0 <= nr < ROWS and

                    0 <= nc < COLS and

                    rooms[nr][nc] == INF):

                    rooms[nr][nc] = rooms[row][col] + 1  

                    q.append((nr, nc))


        # # method 2: Multi Source BFS: time O(M*N); space O(M*N) 

        # ROWS, COLS = len(rooms), len(rooms[0])

        # direction = [[1,0], [-1,0], [0,1], [0,-1]]

        # visit = set() # Need this for level BFS

        # q = deque()

        # for r in range(ROWS):

        #     for c in range(COLS):

        #         if rooms[r][c] == 0:

        #             q.append([r, c])

        #             visit.add((r, c))

        # dist = 0

        # while q:

        #     for i in range(len(q)):

        #         row, col = q.popleft()

        #         rooms[row][col] = dist

        #         for dr, dc in direction: 

        #             nr, nc = row + dr, col + dc

        #             if (0 <= nr < ROWS and 
                    
        #                 0 <= nc < COLS and 

        #                 rooms[nr][nc] != -1 and 

        #                 (nr, nc) not in visit
        #             ): 

        #                 q.append((nr, nc))

        #                 visit.add((nr, nc))

        #     dist += 1


        # method 3: DFS or Backtracking but is slow because this approach reexplores the same areas again and again


# @lc code=end

