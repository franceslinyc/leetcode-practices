#
# @lc app=leetcode id=1610 lang=python3
#
# [1610] Maximum Number of Visible Points
#

from math import atan2, pi

# @lc code=start
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:

        # method sliding window: O(N log N) time; O(N) space
        
        location_x, location_y = location 

        count_same_location = 0 

        angles = []

        for x, y in points: 

            if x == location_x and y == location_y: 

                count_same_location += 1
            
            else: 

                radian = atan2(y - location_y, x - location_x)  # atan2(y, x) return theta

                degree = 180 * radian / pi  # theta / 2 pi = x / 360 -> x = 360 theta / 2 pi = 180 theta / pi

                angles.append(degree)

        angles.sort()

        # Duplicate the angels array to handle wrap-around case
        angles = angles + [a + 360 for a in angles]

        res = 0

        l = 0

        for r in range(len(angles)):

            while angles[r] - angles[l] > angle:

                l += 1

            res = max(res, r - l + 1)

        return res + count_same_location        


# @lc code=end


# e.g., 
# points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1]
# output = 3

# [2,1] -> dx=1, dy=0 -> atan2(0,1) = 0 degree
# [2,2] -> dx=1, dy=1 -> atan2(1,1) = 45
# [3,3] -> dx=2, dy=2 -> atan2(2,2) = 45

# angles = [0, 45, 45]
# angles = [0, 45, 45, 360, 405, 405]

# e.g., 
# points = [[0,0],[0,2]], angle = 90, location = [1,1]

# [0,0] -> dx=-1, dy=-1 -> atan2(-1,-1) = -135
# [0,2,]-> dx=-1, dy=1  -> atan2(1,-1) = 135

# angles = [-135, 135] -> 135 - (-135) = 225 > 90 
# Fail to capture both points
# angles = [-135, 135, 225, 495]
# Now it does capture both points
