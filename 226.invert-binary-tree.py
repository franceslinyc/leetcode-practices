#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # method 1 recursive DFS: O(n) time; O(n) space

        if not root: 

            return None

        # Swap children at current node
        tmp = root.left

        root.left = root.right
        
        root.right = tmp

        # Now fix subtrees
        self.invertTree(root.left)     # After this call, the left subtree is fully inverted

        self.invertTree(root.right)    # After this call, the right subtree is fully inverted
        
        return root


        # # method 1 variation recursive DFS

        # def dfs(current):

        #     if not current: 

        #         return None

        #     tmp = current.left

        #     current.left = current.right

        #     current.right = tmp

        #     dfs(current.left)

        #     dfs(current.right)

        #     return current

        # dfs(root)

        # return root 


        # # method 2 BFS: O(n) time; O(n) space

        # if not root: 

        #     return None
        
        # q = deque([root])

        # while q: 

        #     node = q.popleft()

        #     tmp = node.left
        
        #     node.left = node.right

        #     node.right = tmp

        #     if node.left: 

        #         q.append(node.left)

        #     if node.right: 

        #         q.append(node.right)
    
        # return root


        # # method 3 iterative DFS: O(n) time; O(n) space

        # if not root: 

        #     return None
        
        # s = [root]

        # while s: 

        #     node = s.pop()

        #     tmp = node.left

        #     node.left = node.right

        #     node.right = tmp

        #     if node.left: 

        #         s.append(node.left)

        #     if node.right: 

        #         s.append(node.right)

        # return root

    
# @lc code=end

