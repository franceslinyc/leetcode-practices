#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = defaultdict(set)

        col = defaultdict(set)

        square = defaultdict(set) # key:value = (r // 3,c // 3):board[r][c] 

        for r in range(9): 

            for c in range(9): 

                if board[r][c] != ".": 

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

