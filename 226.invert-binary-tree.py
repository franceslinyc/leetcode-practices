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

        # Fix subtrees; Use self to call the method, but on this specific object
        self.invertTree(root.left)     # After this call, the left subtree is fully inverted

        self.invertTree(root.right)    # After this call, the right subtree is fully inverted
        
        return root


        # # method 1 variation recursive DFS

        # def dfs(node):

        #     if not node: 

        #         return None

        #     tmp = node.left

        #     node.left = node.right

        #     node.right = tmp

        #     dfs(node.left)

        #     dfs(node.right)

        #     return node

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


# We’d solve this with a recursive DFS: at each node, swap its left and right children, 
# then recursively invert both subtrees, returning the root at the end. This runs in O(n) 
# time since we visit every node once, and O(n) space for the recursion stack, where the
# larget height of a tree is n.
