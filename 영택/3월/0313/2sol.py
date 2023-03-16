# leetcode 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/description/
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append((root, root))
        while q:
            l, r = q.popleft()
            if l and r:
                if l.val != r.val:
                    return False
            elif not l and not r:
                continue
            else:
                return False

            q.append((l.left, r.right))
            q.append((l.right, r.left))

        return True