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

        # method 1: dfs: O(n) time; O(n) space

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


# 1. What counts as "valid"? Node value must be strictly inside a range (min, max)
# 2. What do I need from ancestors? Both a floor and a ceiling, i.e., carry min_val/max_val or left/right down
# 3. How does it update? Asymmetric: Going left tightens ceiling to node.val, going right tightens floor to node.val
# 4. What do I return? A bool return True at null, combine with and
# 5. dfs(node, min_val, max_val)


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