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

        # method 1 dfs: O(n) time; O(n) space
        
        def dfs(node, max_val):

            # Base case
            if not node: 

                return 0 

            # Check if current node is good, i.e., a node is good when its value >= max value seen so far 
            # Don't need nonlocal. Does not need to return one thing to its parent but track a different thing as the answer.
            res = 1 if node.val >= max_val else 0 

            # Update max_val before recursing 
            max_val = max(max_val, node.val) 

            # Recursively count good nodes in left and right subtree and sum the counts 
            res += dfs(node.left, max_val) 

            res += dfs(node.right, max_val) 

            return res 

        return dfs(root, root.val)  # dfs(root, float('-inf')) work too
        

        # # method 2: bfs: O(n) time; O(n) space
        
        # res = 0
        
        # q = deque()

        # q.append((root,float('-inf')))

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


# 1. What is the answer?
#    The number of good nodes in the subtree rooted at node.

# 2. Does the child need information from the parent?
#    Yes.
#    The child needs to know what is the maximum value seen from the root to my parent.

# 3. How does it update?
#    max_val = max(max_val, node.val)
#    Each node updates the maximum value seen so far.

# 4. Does the parent need information from the child?
#    Yes.
#    res += dfs(node.left, max_val)
#    res += dfs(node.right, max_val)
#    The parent wants to know how many good nodes are in my left subtree and how many are 
#    in my right subtree.

# 5. dfs(root, root.val) or 
#    dfs(root, float('inf'))