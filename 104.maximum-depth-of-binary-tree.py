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
        
        # method 1 recursive DFS

        if not root: 
            return 0 
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) 

        # # method 2 BFS via queue

        # if not root: 
        #     return 0 
        
        # q = deque([root])

        # level = 0 

        # while q: 
                
        #     for i in range(len(q)): # Process current node    

        #         node = q.popleft()

        #         if node.left: 

        #             q.append(node.left)
                
        #         if node.right: 

        #             q.append(node.right)

        #     level += 1

        # return level

        # # method 3 DFS via stack

        # if not root: 
        #     return 0 
        
        # s = [[root, 1]] 

        # res = 0 

        # while s: 

        #     node, depth = s.pop()

        #     if node: 

        #         res = max(res, depth)
        #         s.append([node.left, depth + 1])
        #         s.append([node.right, depth + 1])

        # return res 

        # Preorder (node first) vs Inorder (node middle) vs Postorder (node last)
        # https://www.geeksforgeeks.org/dsa/preorder-vs-inorder-vs-postorder/
    
# @lc code=end

