# https://leetcode.com/problems/binary-tree-preorder-traversal/
from typing import List, Optional

# 미리 세팅해주셔서 감사합니다 리트코드
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 전위 순회
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []

        def _preorder(root: Optional[TreeNode]) -> None:
            # 더이상 방문할 노드가 없는 경우 반환
            if root is None:
                return
            answer.append(root.val)
            _preorder(root.left)
            _preorder(root.right)

        _preorder(root)
        return answer

# null 때문에 파이참에서 안 돌아가,,import 해야했다.
# print(Solution().preorderTraversal([1,null,2,3]))