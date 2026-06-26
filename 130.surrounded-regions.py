#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # method 2: (Multi-source) BFS: time O(M*N); space O(M*N)

        ROWS, COLS = len(board), len(board[0])

        direction = [[-1,0],[1,0],[0,1],[0,-1]]

        # 1. Put 'O' cells that sit on the border in the queue
        
        q = deque()

        for r in range(ROWS):

            for c in range(COLS):

                if (r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1) and board[r][c] == "O":

                    q.append((r, c))
        
        # 2. Run BFS from 'O' cells that sit on the border, marking everything reachable as "T" (safe)
        
        while q:

            r, c = q.popleft()

            if board[r][c] == "O":

                board[r][c] = "T"

                for dr, dc in direction:

                    nr, nc = r + dr, c + dc

                    if (0 <= nr < ROWS and 
                        
                        0 <= nc < COLS

                    ):

                        q.append((nr, nc))
                        
        # 3. Change every 'O' cell that was never reachable from an 'O' cell on the border to 'X',
        # and every 'T' (safe) cell back to 'O'

        for r in range(ROWS):

            for c in range(COLS):

                if board[r][c] == "O":

                    board[r][c] = "X"

                elif board[r][c] == "T":

                    board[r][c] = "O"        
        

# @lc code=end


# example #1

# row0:  X  X  X  X
# row1:  O  O  X  X
# row2:  X  O  X  X
# row3:  X  X  X  X

# To 

# row0:  X  X  X  X
# row1:  T  T  X  X
# row2:  X  T  X  X
# row3:  X  X  X  X

# example #2

# row0:  X  O  X  X
# row1:  X  O  X  X
# row2:  X  X  X  O
# row3:  X  X  X  O

# To 

# row0:  X  T  X  X
# row1:  X  T  X  X
# row2:  X  X  X  T
# row3:  X  X  X  T

# example #3

# row0:  X  X  X  X
# row1:  X  O  O  X
# row2:  O  O  X  X
# row3:  X  X  X  X

# To

# row0:  X  X  X  X
# row1:  X  T  T  X
# row2:  T  T  X  X
# row3:  X  X  X  X