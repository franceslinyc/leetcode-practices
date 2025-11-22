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

        # method 1 dfs

        # method 2 bfs

        if not root: 

            return []
        
        q = deque([root])

        res = []

        while q: 

            rightside = None #level = []

            for i in range(len(q)): 

                node = q.popleft()

                rightside = node.val #level.append(node.val)

                if node.left: 

                    q.append(node.left)
                
                if node.right: 

                    q.append(node.right)

            res.append(rightside)
            
        return res


# @lc code=end

