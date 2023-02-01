# leetcode 100. Same Tree
# https://leetcode.com/problems/same-tree/description/
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q :
            return True
        if not p or not q :
            return False
        if p.val != q.val :
            return False
        que = deque()
        que.append((p,q))
        while que :
            cp, cq = que.popleft()
            if cp.val != cq.val :
                return False
            if cp.right and cq.right :
                que.append((cp.right,cq.right))
            elif cp.right or cq.right : 
                return False
            if cp.left and cq.left:
                que.append((cp.left, cq.left))
            elif cp.left or cq.left : 
                return False
            
        return True