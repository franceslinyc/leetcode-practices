#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()

        node = dummy 

        carry = 0

        while l1 or l2 or carry: # Add or carry handle edge case when final carry creates a new node

            v1 = l1.val if l1 else 0

            v2 = l2.val if l2 else 0 

            # Compute new digit 

            val = v1 + v2 + carry 

            carry = val // 10    # (8 + 7) // 10 = 1 

            val = val % 10       # (8 + 7) % 10  = 5

            node.next = ListNode(val)

            # Update pointers 

            node = node.next

            l1 = l1.next if l1 else None
            
            l2 = l2.next if l2 else None
        
        return dummy.next


# toy example # 1
#
# l1 = [2,4,3], l2 = [5,6,4]
# output = [7,0,8]
# 
# This is because 
#   3 4 2 
# + 4 6 5
# -------
#   8 0 7
# 
# l1: 2 -> 4 -> 3
# l2: 5 -> 6 -> 4
# -------
#     7 -> 0 -> 8

# toy example # 2
#
# l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# output = [8,9,9,9,0,0,0,1]
# 
# This is because 
#     9 9 9 9 9 9 9 
# +         9 9 9 9 
# -----------------
#     1 0 0 9 9 9 8


# @lc code=end

