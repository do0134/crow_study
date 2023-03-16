# leetcode 129. Sum Root to Leaf Numbers
# https://leetcode.com/problems/sum-root-to-leaf-numbers/
class Solution:
    answer = 0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, num) :
            if not node :
                self.answer += int(num)
                return
            num += str(node.val)
            if node.right :
                dfs(node.right, num)
            if node.left :
                dfs(node.left, num)
            if not node.right and not node.left :
                self.answer += int(num)
        dfs(root, "")
        return self.answer