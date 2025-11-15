#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # # method 1

        # if not root: 
        #     return 0 
        
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) 

        # # method 2 BFS

        # q = deque() 

        # if root: 
        #     q.append(root)

        # level = 0

        # while q: 
                
        #     for i in range(len(q)):     

        #         node = q.popleft()

        #         if node.left: 

        #             q.append(node.left)
                
        #         if node.right: 

        #             q.append(node.right)

        #     level += 1

        # return level

        # method 3 DFS
    
# @lc code=end

