#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # # method 1: brute force: O(m*n) time, m is max # of banana in a pile, and n is length of piles
        # # O(1) space

        # speed = 1 # k bananas per hour

        # while True: # Keep trying indefinitely

        #     total_time = 0 

        #     for pile in piles: 

        #         total_time += math.ceil(pile / speed) # Compute how many hours it takes at current speed, i.e., time = pile / speed
        #                                               # Use ceil because partial hours counts as full hour

        #     if total_time <= h: 

        #         return speed # Exit infinite loop

        #     speed += 1
        
        # return speed

        # method 2 binary search: n * (log m) time, where n is length of piles, and m is max # of bananas in a pile; 
        # O(1) space

        l, r = 1, max(piles)    # Careful! k is in the range [1, max(piles)] 

        res = r   # Worst case. k = max # of bananas in a pile, i.e., eat biggest pile in an hour. 

        # Binary search on k 
        
        while l <= r:           # O(log m) time, m = max(piles)

            k = l + (r - l) // 2

            total_time = 0 

            for pile in piles:  # O(n) time

                total_time += math.ceil(float(pile) / k)

            # Careful! Condition shouldn't be inside for loop.
            
            if total_time <= h:  # If k is fast enough, try smaller k, i.e., [l, k - 1]
                
                res = k 
                
                r = k - 1
            
            else:                # Otherwise, try bigger k, i.e., [k + 1, r]

                l = k + 1

        return res


# @lc code=end

# Idea: 

# piles = [3,6,7,11], h = 8

# time = \sum ⌈ pile / k ⌉

# k = [1, 2, 3, ..., 11]
# k = 11, then h = 4 < 8 valid 
# k = 10, then h = 5 < 8 valid
# ...

# Comment: 

# Can follow leftmost / lower bound template
# Change while l <= r to while l < r
# Change r = k + 1    to r = k still work.
