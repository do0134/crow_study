# leetcode 783. Minimum Distance Between BST Nodes
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        v = set()

        def dfs(tree, v):
            v.add(tree.val)
            if tree.right:
                dfs(tree.right, v)
            if tree.left:
                dfs(tree.left, v)

        dfs(root, v)
        v = sorted(list(v))
        answer = int(1e9)
        for i in range(len(v) - 1):
            answer = min(answer, abs(v[i] - v[i + 1]))
        return answer
