# leetcode 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/description/
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root :
            return
        root.right, root.left = root.left, root.right
        self.invertTree(root.right)
        self.invertTree(root.left)

        return root