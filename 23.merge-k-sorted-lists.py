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

        if not lists: 

            return None
        
        while len(lists) > 1: 

            merge_list = []

            for i in range(0, len(lists), 2): 

                l1 = lists[i]

                if (i + 1) < len(lists): 

                    l2 = lists[i + 1]
                
                else: 

                    l2 = None

                merge_list.append(self.merge_two_lists(l1, l2))

            lists = merge_list 

        return lists[0]
    
    def merge_two_lists(self, l1, l2): 

        dummy = ListNode()

        node = dummy 

        while l1 and l2: 

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

        
# lists = [
#     [1,4,5],   # lists[0]
#     [1,3,4],   # lists[1]
#     [2,6]      # lists[2]
# ]

# Return lists
# [
#     [1,1,2,3,4,4,5,6] 
# ]

# Return lists[0]
# [1,1,2,3,4,4,5,6]
        
        
# @lc code=end

