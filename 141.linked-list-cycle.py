#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        fast, slow = head, head

        while fast and fast.next: # Take care of edge case and ensure that fast.next.next can be accessed, None or not

            # Update before checking if slow == fast. Otherwise, both start at the same ndoe.
            
            slow = slow.next

            fast = fast.next.next

            if slow == fast: 

                return True
            
        return False # Loop finished but no cycle.        
        
# @lc code=end

