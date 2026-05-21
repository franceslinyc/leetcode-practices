#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()  # Anchor the head
                            # Does not move, i.e., stay at the head; dummy: [0] -> None; 

        node = dummy        # Walk the list
                            # Does move; node (or current)

        while list1 and list2: 

            if list1.val < list2.val: 

                node.next = list1

                list1 = list1.next

            else:            # Include list1.val >= list2.val

                node.next = list2

                list2 = list2.next

            node = node.next # Don't forget!

        # Attach the entire list, list1 or list2 

        if list1: 

            node.next = list1

        if list2: 

            node.next = list2

        return dummy.next 
        # dummy.next return [1,1,2,3,4,4]
        #  otherwise return [0,1,1,2,3,4,4]


# dummy
#  |
#  v
# [0] -> None
# 
# dummy
#  |
#  v
# [0] -> [1] -> [1] -> [2] -> [3] -> [4] -> [4] -> None


# @lc code=end

