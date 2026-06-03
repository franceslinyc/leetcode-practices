#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        # method 1 dfs: O(n) time; O(n) space
        
        res = [] # res = ""

        def dfs(node): 

            if not node: 

                res.append("N")

                return      

            res.append(str(node.val)) # Throw a TypeError if not str()

            dfs(node.left)

            dfs(node.right)

            # return res 
        
        dfs(root)

        return ",".join(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        vals = data.split(",")

        i = 0

        def dfs(): 

            nonlocal i 

            if vals[i] == "N": 

                i += 1

                return
            
            node = TreeNode(int(vals[i]))

            i += 1

            node.left = dfs()

            node.right = dfs()

            return node
        
        return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

