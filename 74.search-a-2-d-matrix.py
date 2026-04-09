#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # # method 1 binary search: O(log m + log n) time; O(1) space

        # ROWS, COLS = len(matrix), len(matrix[0])
        
        # top, bottom = 0, ROWS - 1 

        # while top <= bottom: 

        #     row = (top + bottom) // 2

        #     if matrix[row][0] <= target <= matrix[row][-1]: 

        #         l, r = 0, COLS -1 
       
        #         while l <= r:             # LC 704 

        #             m = (l + r) // 2

        #             if matrix[row][m] == target: 

        #                 return True
                    
        #             elif matrix[row][m] > target: # Narrow search to [l, m - 1]

        #                 r = m - 1
                    
        #             else:                         # Narrow search to [m + 1, r]

        #                 l = m + 1
                
        #         return False              # Not found in this row; Return -1 for LC 704 

        #     elif matrix[row][0] > target:         # Narrow search to [top, row - 1]

        #         bottom = row - 1

        #     else: # elif matrix[row][-1] < target:        # Narrow search to [row + 1, bottom]

        #         top = row + 1

        # return False                     # Not found in any row

        # method 1 binary search: O(log m + log n) time, which reduces to O(log(m*n)); O(1) space

        ROWS, COLS = len(matrix), len(matrix[0])

        top, bottom = 0, ROWS - 1

        while top <= bottom:

            row = (top + bottom) // 2

            if target > matrix[row][-1]:

                top = row + 1

            elif target < matrix[row][0]:

                bottom = row - 1

            else:

                break

        if not (top <= bottom):

            return False

        row = (top + bottom) // 2

        l, r = 0, COLS - 1

        while l <= r:

            m = (l + r) // 2

            if target > matrix[row][m]:

                l = m + 1

            elif target < matrix[row][m]:

                r = m - 1

            else:

                return True

        return False        


        # method 2 binary search (one pass): O(log(m*n)) time; O(1) space


# @lc code=end

