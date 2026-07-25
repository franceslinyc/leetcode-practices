#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # # method 1 dfs: O(n) time worst case, O(log n) time best case for balanced tree; O(n) space

        # # Base case 1: If both nodes are None, they are same.

        # if not p and not q: 

        #     return True

        # # Base case 2: If both nodes exist AND their values are equal, we still need to check their subtrees.

        # if p and q and p.val == q.val: 

        #     # Recrusively check left and right subtree of both trees
        #     return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # # Base case 3: If one is None while the other is not, or both exist but their values differ, they are not the same.

        # else: 

        #     return False


        # method 2 bfs: O(n) time; O(n) space

        q1 = deque([p])
        
        q2 = deque([q])

        # Traverse both trees in parallel
        while q1 and q2:

            # Process all nodes at the current level
            for _ in range(len(q1)):
                
                node_1 = q1.popleft()
                
                node_2 = q2.popleft()

                # Case 1: both nodes are None -> structurally same at this position
                if not node_1 and not node_2: 

                    continue

                # Case 2, 3: Either one is None or value differs -> different 
                if not node_1 or not node_2 or node_1.val != node_2.val: 

                    return False

                # Add children for further comparison
                # Careful! None is meaningful, do not use if node_1.left to check. ALWAYS append. 

                q1.append(node_1.left)

                q1.append(node_1.right)

                q2.append(node_2.left)

                q2.append(node_2.right)

        return True


# @lc code=end

