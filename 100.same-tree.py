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

        # if not q and not p: 

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
                
                node_p = q1.popleft()
                
                node_q = q2.popleft()

                # Case 1: both nodes are None -> structurally same at this position
                #if node_p is None and node_q is None:
                if not node_p and not node_q: 

                    continue

                # Case 2: Either one is None -> different 
                #if node_p is None or node_q is None:
                if not node_p or not node_q: 

                    return False

                # Case 3: Value differ -> different 
                if node_p.val != node_q.val: 

                    return False

                # Add children for further comparison
                # Careful! None is meaningful, do not use if node_p.left to check. ALWAYS append. 

                q1.append(node_p.left)

                q1.append(node_p.right)

                q2.append(node_q.left)

                q2.append(node_q.right)

        return True


# @lc code=end

