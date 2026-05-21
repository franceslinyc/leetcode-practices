#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # method 3 divide and conquer, iteration: O(N log K) time, where K is total # of lists and N is total # of nodes; O(1) space
        
        if not lists:         # Handle [] or none

            return None
        
        while len(lists) > 1: # log K time: Halve each round

            merge_list = []  

            for i in range(0, len(lists), 2):   # Grab pairs 

                l1 = lists[i]

                if (i + 1) < len(lists): 

                    l2 = lists[i + 1]    # Even list: l2 has a pair
                
                else: 

                    l2 = None            # Odd list: Last list unpaired, carries forward

                merge_list.append(self.merge_two_lists(l1, l2)) # O(N) combined time

            lists = merge_list 

        return lists[0]     # Careful! 
    
    def merge_two_lists(self, l1, l2): 

        # LC 21 
        
        dummy = ListNode()

        node = dummy 

        while l1 and l2: # O(M + N) time

            if l1.val < l2.val: 

                node.next = l1

                l1 = l1.next
            
            else: 

                node.next = l2

                l2 = l2.next
            
            node = node.next

        if l1: 

            node.next = l1
        
        if l2: 

            node.next = l2

        return dummy.next


# @lc code=end


# lists = [
#     [1,4,5],   # lists[0]
#     [1,3,4],   # lists[1]
#     [2,6]      # lists[2]
# ]

# round 1: 
# merge_list = [[1,1,3,4,4,5], [2,6]] # (lists[0], lists[1]) paired; (lists[2], None) paired

# round 2: 
# merge_list = [[1,1,2,3,4,4,5,6]]    # (lists[0], lists[1]) paired

# Return lists
# [
#     [1,1,2,3,4,4,5,6] 
# ]

# Return lists[0]
# [1,1,2,3,4,4,5,6]
