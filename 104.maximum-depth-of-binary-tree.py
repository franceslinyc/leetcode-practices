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
        
        # method 1 recursive DFS: O(n) time worst case, O(log n) best case; O(n) space

        if not root: 

            return 0 
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


        # # method 1 variation recursive DFS

        # self.max_depth = 0

        # def dfs(current, depth): 

        #         if not current: 

        #                 return 

        #         self.max_depth = max(self.max_depth, depth) 

        #         dfs(current.left, depth + 1)

        #         dfs(current.right, depth + 1)

        # dfs(root, 1)

        # return self.max_depth


        # # method 2 BFS via queue: O(n) time; O(n) space

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


# 3 9 20 15 7
# 1 2 2  3  3


        # # method 3 DFS via stack: O(n) time; O(n) space

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


# 7  3
# 15 3
# 20 2
# 9  2
# 3  1


# Preorder (node first) vs Inorder (node middle) vs Postorder (node last)
# https://www.geeksforgeeks.org/dsa/preorder-vs-inorder-vs-postorder/


# We’d use a recursive DFS: at each node, compute the max depth of its left and right subtrees 
# and return max(left, right) + 1, with the base case returning 0 for null nodes. This runs in 
# O(n) time since every node is visited once, and O(n) space for the recursion stack, where 
# O(log n) for best case balanced tree, and O(n) for worst case.
    
    
# @lc code=end

