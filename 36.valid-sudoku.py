#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = defaultdict(set)      # or row = [set() for _ in range(9)]

        col = defaultdict(set)      # or col = [set() for _ in range(9)]

        square = defaultdict(set)   # or square = [[set() for _ in range(3)] for _ in range(3)]
                                    # key:value = (r // 3,c // 3):board[r][c] 

        for r in range(9): 

            for c in range(9): 

                if board[r][c] == ".": 

                    continue

                if (board[r][c] in row[r] or 

                    board[r][c] in col[c] or 

                    board[r][c] in square[(r // 3, c // 3)]

                ): 

                    return False

                row[r].add(board[r][c])

                col[c].add(board[r][c])

                square[(r // 3, c // 3)].add(board[r][c])

        return True

             
# @lc code=end



# 5 3 . | . 7 . | . . .
# 6 . . | 1 9 5 | . . .
# . 9 8 | . . . | . 6 .

# row = {
#     0: {'5', '3', '7'},
#     1: {'6', '1', '9', '5'},
#     2: {'9', '8', '6'},
# }

# col = {
#     0: {'5', '6'},
#     1: {'3', '9'},
#     2: {'8'},
#     3: {'1'},
#     4: {'7', '9'},
#     5: {'5'},
#     6: set(),   # no non-'.' value seen yet in col 6
#     ...
#     8: {'6'},
# }

# square = {
#     (0, 0): {'5', '3', '6', '9', '8'},   # cells from rows 0-2, cols 0-2
#     (0, 1): {'7', '1', '9', '5'},        # rows 0-2, cols 3-5
#     (0, 2): set(),                       # rows 0-2, cols 6-8, all '.'
# }

# Need a function that takes any row (or col) index 0-8 and outputs which "band" of 3 it falls into — 0, 1, or 2 — so that:

# indices 0, 1, 2 → band 0
# indices 3, 4, 5 → band 1
# indices 6, 7, 8 → band 2