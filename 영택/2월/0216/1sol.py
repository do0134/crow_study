# leetcode 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(tree, depth):
            if not tree:
                return depth

            r = dfs(tree.right, depth + 1)
            l = dfs(tree.left, depth + 1)

            return max(r, l)

        return dfs(root, 0)