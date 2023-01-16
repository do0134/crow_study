# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/
from collections import defaultdict
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # https://xingxingpark.com/Leetcode-1061-Lexicographically-Smallest-Equivalent-String/
        neighbors = defaultdict(set)
        for a, b in zip(s1, s2):
            neighbors[a].add(b)
            neighbors[b].add(a)

        memo = {}

        def bfs(chr):
            if chr in memo:
                return memo[chr]
            res = chr
            seen = set()
            queue = {chr}

            while queue:
                c = queue.pop()
                if c in seen:
                    continue
                seen.add(c)
                res = min(res, c)
                queue |= neighbors[c]

            for v in seen:
                memo[v] = res

            return res
        return ''.join(bfs(c) for c in baseStr)

print(Solution().smallestEquivalentString("parker", "morris", "parser"))