class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        if not roads:
            return 0

        tree = defaultdict(list)

        for i, j in roads:
            tree[i].append(j)
            tree[j].append(i)

        self.answer = 0

        def dfs(i, prev, people=1):
            for x in tree[i]:
                if x == prev: continue
                people += dfs(x, i)
            self.answer += (int(ceil(people / seats)) if i else 0)
            return people

        dfs(0, 0)
        return self.answer