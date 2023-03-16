# leetcode 106. Construct Binary Tree from Inorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder :
            return None

        c_val = postorder.pop()
        tree = TreeNode(c_val)

        mid = inorder.index(c_val)

        tree.right = self.buildTree(inorder[mid+1:],postorder)
        tree.left = self.buildTree(inorder[:mid],postorder)
        return tree