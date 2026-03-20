#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start
class NumMatrix:

    # method 1: Brute Force

    # def __init__(self, matrix: List[List[int]]):

    #     self.matrix = matrix
        
    # def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
    #     res = 0
        
    #     for r in range(row1, row2 + 1):       # Careful! range(start, end) is exclusive of end

    #         for c in range(col1, col2 + 1):

    #             res += self.matrix[r][c]

    #     return res


    # method 2: One Dimensional Prefix Sum

    # method 3: Two Dimensional Prefix Sum

    def __init__(self, matrix: List[List[int]]):

        ROWS, COLS = len(matrix), len(matrix[0])

        self.sum_matrix = [[0] * (COLS + 1) for r in range(ROWS + 1)]    # + 1 to include 0

        for r in range(ROWS): 

            prefix = 0 

            for c in range(COLS): 

                prefix += matrix[r][c]               # Row sum or prefix sum for each row; Read value; Similar to current += num in LC 303

                above = self.sum_matrix[r][c + 1]    # Above = [prev row][current col]; Reuse computed sum

                self.sum_matrix[r + 1][c + 1] = prefix + above


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1 # Adjust for index shifting

        bottom_right = self.sum_matrix[row2][col2]

        above = self.sum_matrix[row1 - 1][col2]

        left = self.sum_matrix[row2][col1 - 1]

        top_left = self.sum_matrix[row1 - 1][col1 - 1]

        return bottom_right - above - left + top_left


#    3  0
#    5  6

# 0  0  0
# 0  ?  ?
# 0  ?  ?

# 0  0  0
# 0  3  3, where 3 is 3 (prefix) + 0 (above) and 3 is 3 (prefix) + 0 (above)
# 0  0  0

# 0  0  0
# 0  3  3
# 0  8  14, where 8 is 5 (prefix) + 3 (above) and 14 is 11 (prefix) + 3 (above)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

