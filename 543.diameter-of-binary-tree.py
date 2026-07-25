#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # method 1 recursive DFS: O(n) time worst case, O(log n) best case; O(n) space; post-order traversal

        diameter = 0 

        def dfs(node): 

            nonlocal diameter
            
            # Base case: empty node has height 0
            if not node: 

                return 0 

            # Recursively find height of left and right subtrees
            left = dfs(node.left)        
            
            right = dfs(node.right)

            # Update diameter
            diameter = max(diameter, left + right) 

            # Return height of current node to parent, i.e., max height of children + 1 (edge to parent) 
            return max(left, right) + 1
        
        dfs(root)

        return diameter


        # method 2 DFS with Stack: O(n) time; O(n) space


# @lc code=end


# Every "best path in a tree" problem has this split:
# 1. Best path through node — use both branches, bend here, update global answer
# 2. Best single branch — picks one side, return to parent so it can do its calculation


# 1. What is the answer?
#    The longest path (in edges) between any two nodes.

# 2. Does the child need information from the parent?
#    No.
#    No extra parameter.

# 3. How does it update?
#    diameter = max(diameter, left_height + right_height)
#    because the longest path through this node uses both branches.

# 4. Does the parent need information from the child?
#    Yes.
#    Return the subtree height:
#    max(left_height, right_height) + 1

# 5. dfs(node)
#    Returns the height of the subtree rooted at node.