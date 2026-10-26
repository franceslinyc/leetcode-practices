#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # # method 1 quick sort: O(n log n) average time, O(n^2) worst case; O(log n) recursive stack; Time Limit Exceeded

        # def partition(arr, L, R): 

        #     pivot = arr[R]

        #     lo = L

        #     for i in range(L, R): 

        #         if arr[i] < pivot: 

        #             arr[lo], arr[i] = arr[i], arr[lo]

        #             lo += 1

        #     arr[lo], arr[R] = arr[R], arr[lo]

        #     return lo

        # def quick_sort(arr, l, r): 

        #     if l >= r: 
                
        #         return

        #     pivot_index = partition(arr, l, r)

        #     quick_sort(arr, l, pivot_index - 1)

        #     quick_sort(arr, pivot_index + 1, r)

        # quick_sort(nums, 0, len(nums) - 1)

        # return nums

        # # method 2 merge sort: O(n log n) time; O(n) space

        # # Merge two sorted halves 
        # def merge(arr, L, M, R):

        #     left, right = arr[L:M+1], arr[M+1:R+1]   # O(n) space worst case
        #                                              # string[start:end]; start is inclusive, end is not
              
        #     # i = pointer for main array
        #     # j = pointer for left half
        #     # k = pointer for right half
        #     i, j, k = L, 0, 0

        #     # Merge both arrays
        #     while j < len(left) and k < len(right):

        #         if left[j] <= right[k]:

        #             arr[i] = left[j]

        #             j += 1

        #         else:

        #             arr[i] = right[k]

        #             k += 1

        #         i += 1

        #     # Copy remaining elements from left
        #     while j < len(left):

        #         arr[i] = left[j]

        #         j += 1

        #         i += 1

        #     # Copy remaining elements from right
        #     while k < len(right):

        #         arr[i] = right[k]

        #         k += 1

        #         i += 1

        # def merge_sort(arr, l, r):

        #     # Base case: one element
        #     if l >= r:   # l>= r is safer; if l == r handle only valid single-element case

        #         return

        #     m = (l + r) // 2

        #     # Now sort subarrays; log n levels of recursion
        #     merge_sort(arr, l, m)         # After this call, the left half, i.e., arr[l:m+1], is sorted

        #     merge_sort(arr, m + 1, r)     # After this call, the right half, i.e., arr[m+1:r+1], is sorted

        #     # Merge sorted halves; O(n) time
        #     merge(arr, l, m, r)

        # merge_sort(nums, 0, len(nums) - 1) # n time
        
        # return nums


        # method 3 heap sort: O(n log n) time; O(log n) recursive stack


        # method 4 counting sort: O(n + k) time; O(n) space

        def counting_sort():

            count = defaultdict(int)

            min_num, max_num = min(nums), max(nums)

            for num in nums:

                count[num] += 1

            index = 0

            for num in range(min_num, max_num + 1):

                while count[num] > 0:

                    nums[index] = num

                    index += 1

                    count[num] -= 1

        counting_sort()

        return nums        


        # method 4 counting sort variation: O(n + k) time; O(n) space



# @lc code=end

# Merge sort idea: 

# 1. Recursively SORT left half
# 2. Recursively SORT right half
# 3. MERGE the two sorted halves
# i.e., go down (split) -> reach bottom -> come back up (merge)

# Example: [5, 2, 3, 1]

# Step 1: First split
# nums = [5, 2, 3, 1]
# merge_sort(nums, 0, 3)
# l = 0, r = 3 -> m = 1
# left half = [5, 2], right half = [3, 1]

# Step 2: Solve LEFT half
# [5, 2, 3, 1]
#  0, 1, 2, 3 
# Focus on [5, 2]
# merge_sort(nums, 0, 1)
# l = 0, r = 1 -> m = 0
# Now [5] and [2]
# merge_sort(0,0) -> return
# merge_sort(1,1) -> return
# NOW merge(nums, 0,0,1), i.e., merge nums[0:1] (i.e., [5]) and nums[1:2] (i.e., [2])
# [2, 5]

# Step 3: Solve RIGHT half
# [5, 2, 3, 1]
#  0, 1, 2, 3 
# Focus on [3, 1]
# merge_sort(nums, 2, 3)
# l = 2, r = 3 -> m = 2
# Now [3] and [1]
# merge_sort(2,2) -> return
# merge_sort(3,3) -> return
# NOW merge(nums, 2,2,3), i.e., merge nums[2:3] (i.e., [3]) and nums[3:4] (i.e., [1])
# [1, 3]

# Step 4: Final merge
# left  = [2, 5]
# right = [1, 3]
# [1, 2, 3, 5]


# Counting sort idea:  

# Example: [5, 1, 1, 2, 0, 0]

# Step 1: find the range
#   min_num, max_num = 0, 5
#   output: range to walk is 0, 1, 2, 3, 4, 5

# Step 2: count occurrences
#   for num in nums: count[num] += 1
#   output: count = {5: 1, 1: 2, 2: 1, 0: 2}   (first-seen order, not sorted)

# Step 3: walk min..max, write each value back count[num] times
#   num = 0 -> count 2 -> write 0, 0   nums = [0, 0, _, _, _, _]
#   num = 1 -> count 2 -> write 1, 1   nums = [0, 0, 1, 1, _, _]
#   num = 2 -> count 1 -> write 2      nums = [0, 0, 1, 1, 2, _]
#   num = 3 -> count 0 -> skip
#   num = 4 -> count 0 -> skip
#   num = 5 -> count 1 -> write 5      nums = [0, 0, 1, 1, 2, 5]
#   output: [0, 0, 1, 1, 2, 5]