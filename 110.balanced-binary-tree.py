#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # method 1 recursive DFS: O(n) time; O(h) space, where h is height, O(log n) best case for balanced tree, O(n) worst case        
        
        def dfs(node): 

            # Base case: an empty node is balanced with height 0
            if not node: 

                return [True, 0] 

            # Recursively check left and right subtrees 
            left = dfs(node.left)

            right = dfs(node.right)

            # Check whether left subtree is balanced
            # Check whether right subtree is balanced
            # Check whether current node is balanced, i.e., height difference is <= 1
            # left[1] -> height of left subtree
            # right[1] -> height of right subtree
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            # Return height of parent (current) node = max height of children + 1 
            return [balanced, max(left[1], right[1]) + 1]

        return dfs(root)[0]


        # # method 1 variation recursive DFS via coding inverview pattern

        # def dfs(node): 

        #     if not node: 

        #         return 0

        #     left = dfs(node.left)

        #     right = dfs(node.right)

        #     if left == -1 or right == -1: 

        #         return -1

        #     if abs(left - right) > 1: 

        #         return -1

        #     return max(left, right) + 1   # Return height if balanced. Else, return -1. 

        # return dfs(root) != -1
        

        # method 2 iterative DFS: O(n) time; O(n) space


# @lc code=end


# 1. What is the answer?
#    Whether every node in the tree is height-balanced.

# 2. Does the child need information from the parent?
#    No.
#    No extra parameter.

# 3. How does it update?
#    balanced = (
#        left_balanced
#        and right_balanced
#        and abs(left_height - right_height) <= 1
#    )
#    because both subtrees must be balanced and their heights
#    can differ by at most 1. 

# 4. Does the parent need information from the child?
#    Yes.
#    Return whether the subtree is balanced and its height:
#    [balanced, max(left_height, right_height) + 1]

# 5. dfs(node)
#    Returns [balanced, height] of the subtree rooted at node.
