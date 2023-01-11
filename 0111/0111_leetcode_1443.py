#
from typing import List
from collections import defaultdict

# 양심고백: 모르겠어서 답 봤습니다,,
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # 인접 노드 표시하려고 딕셔너리로 만든다!
        # 그래서 최상위 노드 제외하고는 부모 노드가 포함됨
        # ex: defaultdict(<class 'list'>, {0: [1, 2], 1: [0, 4, 5], 2: [0, 3, 6], 4: [1], 5: [1], 3: [2], 6: [2]})
        tree = defaultdict(list)
        # 양방향 트리 (start, end)
        for s, e in edges:
            tree[s].append(e)
            tree[e].append(s)
        def dfs(node, parent):

            # 최상위 노드에서부터 모든 사과를 찍고 돌아오는 최소 시간
            res = 0

            # 트리라서 사이클 없음
            # 양방향이기 때문에 인접 노드 중 하나가 상위 노드
            for neighbor in tree[node]:
                # 상위 노드로 돌아가지 않게 조건 달기
                if neighbor != parent:
                    res += dfs(neighbor, node)

            # 1. res != 0: 트리 아래에 사과 있음
            # 2. hasApple[node] == True: 현재 노드에 사과 있음
            # 두 경우 결과에 2를 늘려야 한다. (방문했다가(+1) 돌아간다는(+1) 뜻)
            if res or hasApple[node]:
                return res + 2
            # 이 노드나 트리 아래 사과가 없는 경우 노드 이동이 없으니 0 반환됨
            return res

        # 최상위 노드 때문에 2가 추가로 더해지기 때문에 2를 뺀다.
        # 사과가 없을 경우 -2가 되는데 아웃풋 조건이 0이므로 디폴트값을 0으로 준다.
        return max(dfs(0, -1) - 2, 0)

print(Solution().minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,True,True,False]))