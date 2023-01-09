# leetcode 144. Binary Tree Preorder Traversal
# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        def pre(node,answer) :
            if not node :
                return []
            answer.append(node.val)
            pre(node.left,answer)
            pre(node.right,answer)
        pre(root,answer)
        return answer
        