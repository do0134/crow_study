from typing import Optional, List

import null as null


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 같은 트리인가용?
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # answer = "false"
        # 이거 파이참에서는 예제 답 잘 나오는데 리트코드에서 안됨 와이?
        # if p == q:
        #     answer = "true"
        # return answer

        # 인터넷에 찾아보니 노드자식도 비교하래서 해봅니다.
        # 순회하려고 했는데 이런 것도 된데서 해봄
        # 더 이상 방문할 노드가 없을 때 (끝까지 순회했으니까 다 똑같음)
        if p == None and q == None:
            return True
        elif p != None and q != None:
            # 첫 노드가 같을 때
            if p.val == q.val:
                # 재귀해서 자식 노드들 비교
                # self 인자 있을 때 재귀는 이렇게 하는구나
                # 조건을 반대로 주니까 예외가 나오는데 왜 그러는지 잘 모르겠습니다...
                if not self.isSameTree(p.left, q.left):
                    return False
                elif not self.isSameTree(p.right, q.right):
                    return False
                else:
                    return True
            # 니는 이미 끝났다
            else:
                return False
# p: Optional[TreeNode] = [1,2,3]
# q: Optional[TreeNode] = [1,2,3]
# print(Solution().isSameTree(p, q))
# 아 왜 또 안 돌아갑니까?