# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/
from typing import List
from collections import defaultdict

# 풀이 봤는데도 모르겠음
class Solution:
    # 문자가 다른 노드들을 통과하는 최대 경로?
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = defaultdict(list)

        # end: index(node), start: parent
        for end, start in enumerate(parent):
            tree[start].append(end)

        # root
        res = 1
        def dfs(node):
            nonlocal res

            # 이거 왜 두 개 구하지?
            max1 = max2 = 0

            for nei in tree[node]:
                neiL = dfs(nei)
                if s[nei] != s[node]:
                    if neiL > max1:
                        max2 = max1
                        max1 = neiL
                    elif neiL > max2:
                        max2 = neiL
            # max1 + max2 + 1: 가장 긴 경로 (유효한 경로를 축적 중)
            # 현재 노드가 이 노드에서 뿌리 내린 하위 트리를 통과하는 중이다..
            res = max(res, max1 + max2 + 1)

            # 현재 노드 때문에 1 추가
            return max1 + 1
        dfs(0)
        return res

print(Solution().longestPath([-1,0,0,1,1,2], "abacbe"))