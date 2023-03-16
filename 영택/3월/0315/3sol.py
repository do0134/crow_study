# leetcode 958. Check Completeness of a Binary Tree
# https://leetcode.com/problems/check-completeness-of-a-binary-tree/
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)
        flag = False
        while q:
            n = len(q)

            for _ in range(n):
                node = q.popleft()
                if not node:
                    flag = True
                    continue
                if flag:
                    return False
                q.append(node.left)
                q.append(node.right)

        return True