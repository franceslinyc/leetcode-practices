#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # method 1: two pointers; time O(n^2), where n is length of the given array; space O(1) + O(n) for sort() excluding output list. 
        # If including output list, space O(m) and O(n^2) worst case, where m is the number of unique triplet.

        nums.sort() # O(n log n) time but O(n log n) < O(n^2); O(n) space

        res = []

        for i, num in enumerate(nums): # O(n)

            if num > 0:  # Array is sorted. If the first number is > 0, the rest cannot sum to 0

                break    # Exit for loop
            
            if i > 0 and num == nums[i - 1]:   # Skip duplicate values for the first number (nums[i]) to avoid duplicate triplets

                continue # i advances to i + 1

            # Two pointer search for the remaining two numbers; Similar to LC 167 Two Sum II
            
            l, r = i + 1, len(nums) - 1 

            while l < r:              # O(n) worst case

                current_sum = num + nums[l] + nums[r]
                
                if current_sum == 0: 

                    res.append([num, nums[l], nums[r]])
                 
                    # Move both pointers inward to look for new pairs

                    l += 1 

                    r -= 1

                    # Skip duplicates for the left pointer
                    
                    while l < r and nums[l] == nums[l - 1]: # Careful! nums[l-1] is the value just used in the triplet; nums[l] is the new updated value

                        l += 1

                    # # (Optional) Skip duplicates for the right pointer

                    # while l < r and nums[r] == nums[r + 1]: 

                    #     r -= 1                    

                elif current_sum < 0: 

                    l += 1

                else: 

                    r -= 1
            
        return res 


        # method 2: hash map; time O(n^2); space O(n)


# @lc code=end

