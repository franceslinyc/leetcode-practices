#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#

# @lc code=start
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        # method 4: binary search + two pointers: O(log n + k) time; O(k) space, where k is the # of closest elements to find 
        
        # binary search + greedy expansion around a pivot

        # Find the leftmost position
        
        l, r = 0, len(arr) - 1

        while l < r:

            mid = (l + r) // 2
            
            if arr[mid] < x:

                l = mid + 1

            else:

                r = mid

        l, r = l - 1, l    # Let l point to the left of this leftmost position and r point to the leftmost position

        # While have fewer elements than k, expand outward to collect k closest elements

        while r - l - 1 < k:

            if l < 0:

                r += 1

            elif r >= len(arr):

                l -= 1

            elif abs(arr[l] - x) <= abs(arr[r] - x):

                l -= 1

            else:

                r += 1

        return arr[l + 1: r]        
        

        # # method 5: binary search: O(log (n - k) + k) time; O(k) space, where k is the # of closest elements to find 

        # # binary search over sliding window positions

        # # Find the starting position of the k-length window 

        # l, r = 0, len(arr) - k

        # while l < r: 

        #     m = (l + r) // 2

        #     if x - arr[m] > arr[m + k] - x: 

        #         l = m + 1
            
        #     else: 

        #         r = m

        # return arr[l: l + k]


# @lc code=end

