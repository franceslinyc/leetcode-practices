#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # method 1 dfs: O(n) time; O(n) space

        def dfs(node, min_val, max_val): 

            # Base case
            if not node: 

                return True

            # Check if current node is within valid range
            if not (min_val < node.val < max_val): 

                return False

            # Recursively check if left and right subtree is valid with updated range
            return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)

        return dfs(root, float("-inf"), float("inf"))
    

        # # method 2 bfs

        # if not root: 

        #     return None
        
        # q = deque([(root, float("-Inf"), float("Inf"))]) # Careful! []

        # while q: 

        #     node, left, right = q.popleft()

        #     if not (left < node.val < right): 

        #         return False
            
        #     if node.left: 

        #         q.append((node.left, left, node.val)) 
            
        #     if node.right: 

        #         q.append((node.right, node.val, right))
        
        # return True


# @lc code=end


# 1. What is the answer?
#    Whether the subtree rooted at node is a valid BST, i.e., whether
#    node value inside a valid range value (min, max). 

# 2. Does the child need information from the parent?
#    Yes. The child needs the valid range value (min_val, max_val)
#    determined by all its parents.

# 3. How does the current node update that information?
#    Left child:  (min_val, node.val)
#    Right child: (node.val, max_val)

# 4. Does the parent need information from the child?
#    Yes.
#    A boolean: Is the left subtree valid?
#               Is the right subtree valid?
#    Parent combines them with: left_valid and right_valid

# 5. What does dfs(node, min_val, max_val) mean?
#    Returns whether the subtree rooted at node is a valid BST,
#    assuming every node must satisfy: min_val < node.val < max_val


#   5
#  / \
# 1   7
#    / \
#   3   8   ← 3 < 5, violates BST even though 3 > parent 7's... wait, no

# dfs(5, -inf, inf)   ✓
#   dfs(1, -inf, 5)   ✓
#   dfs(7, 5, inf)    ✓
#     dfs(3, 5, inf)  ✗  ← 3 is not within (5, inf)
#     return False

#   5
#  / \
# 1   7
#    / \
#   6   8   ← yes