#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # method 1 binary search

        rows = len(matrix)
        cols = len(matrix[0])
        top = 0 
        bottom = rows - 1 

        while top <= bottom: 

            row = (top + bottom) // 2

            if matrix[row][0] <= target <= matrix[row][-1]: 

                l = 0 

                r = cols -1 

                while l <= r: 

                    m = (l + r) // 2

                    if matrix[row][m] == target: 

                        return True
                    
                    elif matrix[row][m] > target: 

                        r = m - 1
                    
                    else: 

                        l = m + 1
                
                return False # Not found in this row

            elif matrix[row][0] > target: 

                bottom = row - 1

            elif matrix[row][-1] < target:

                top = row + 1

        return False       # Not found in any row

        # method 2 binary search (one pastt)


# @lc code=end

