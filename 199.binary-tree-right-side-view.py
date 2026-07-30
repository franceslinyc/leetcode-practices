#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # # method 1 DFS: time O(n), space O(n), where n: # of nodes 

        # res = []

        # def dfs(node, depth): 

        #     # Base case
        #     if not node: 

        #         return None
            
        #     # Because we go right first, this will be the right most node. 
            
        #     if depth == len(res):      # If this is the first time reaching this depth, store it
                
        #         res.append(node.val)
            
        #     # Important! Visit right first 
        #     # Recurse to the right (first) and left child by increasing depth
            
        #     dfs(node.right, depth + 1)

        #     dfs(node.left, depth + 1)
        
        # # Start dfs from root at depth 0 
        
        # dfs(root, 0)

        # return res 


        # method 2 BFS: time O(n), space O(n), where n: # of nodes; balanced BFS -> time O(log n)

        if not root: 

            return []
        
        q = deque([root])

        res = []

        while q: 

            rightside = None         # vs LC 102 level = [] 

            for i in range(len(q)): 

                node = q.popleft()

                rightside = node.val # Keep overwriting; vs LC 102 level.append(node.val) store the entire level

                if node.left: 

                    q.append(node.left)
                
                if node.right: 

                    q.append(node.right)

            res.append(rightside)    # Safer to add instead of adding node.val directly 
            
        return res


# @lc code=end

