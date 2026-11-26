# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        return self.invertNodes(root)
    def invertNodes(self,node):
        if not node:
            return
        node.left, node.right = node.right, node.left
        self.invertNodes(node.left)
        self.invertNodes(node.right)
        return node

