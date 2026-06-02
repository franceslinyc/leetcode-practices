#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # method 1: dfs: O(n) time; O(n) space
        
        def dfs(node, max_val):

            # Base case
            if not node: 

                return 0 

            # Check if current node is good, i.e., a node is good when its value >= max value seen so far 
            res = 1 if node.val >= max_val else 0 

            # Update max_val before recursing 
            max_val = max(max_val, node.val) 

            # Recursively count good nodes in left and right subtree and sum the counts 
            res += dfs(node.left, max_val) 

            res += dfs(node.right, max_val) 

            return res 

        return dfs(root, root.val) 
        

        # # method 2: bfs: O(n) time; O(n) space
        
        # res = 0
        
        # q = deque()

        # q.append((root,-float('inf')))

        # while q:

        #     node, max_val = q.popleft()

        #     if node.val >= max_val:

        #         res += 1

        #     if node.left:

        #         q.append((node.left, max(max_val,node.val)))

        #     if node.right:

        #         q.append((node.right, max(max_val,node.val)))

        # return res


# @lc code=end


# 1. What counts as "good"? Node value >= max value seen on path from root to it
# 2. What do I need from ancestors? The running maximum, i.e., carry max_val down
# 3. How does it update? max(max_val, node.val)
# 4. What do I return? A count return 0 at null, accumulate with + 
# 5. dfs(node, max_val)