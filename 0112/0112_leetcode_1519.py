# https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/
from typing import List
from collections import defaultdict, Counter

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        # 인접 노드 딕셔너리
        tree = defaultdict(list)
        answer = [0] * n

        # 양방향 트리
        for s, e in edges:
            tree[s].append(e)
            tree[e].append(s)

        def dfs(node, parent):
            # 라벨이 문자라서 딕셔너리
            count = Counter()
            # 양방향이기 때문에 인접 노드 중 하나가 상위 노드
            for neighbor in tree[node]:
                # 상위 노드로 돌아가지 말아줘
                if neighbor != parent:
                    count += dfs(neighbor, node)

            # 라벨 갯수 카운트에 추가
            count[labels[node]] += 1
            # 답 리스트에 인접 노드 라벨 카운트 기록
            answer[node] = count[labels[node]]
            return count

        dfs(0, -1)
        return answer

print(Solution().countSubTrees(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], "abaedcd"))