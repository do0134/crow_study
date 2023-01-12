# leetcode 1519. Number of Nodes in the Sub-Tree With the Same Label
# https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/description/

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        answer = [0] * n
        tree = [[] * n for _ in range(n)]

        for i, j in edges:
            tree[i].append(j)
            tree[j].append(i)

        def dfs(p, n):
            cnt = Counter()
            for i in tree[n]:
                if i == p:
                    continue
                else:
                    cnt += dfs(n, i)
            cnt[labels[n]] += 1
            answer[n] = cnt[labels[n]]
            return cnt

        dfs(-1, 0)
        return answer