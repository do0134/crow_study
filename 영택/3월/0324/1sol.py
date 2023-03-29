# leetcode 1466. Reorder Routes to Make All Paths Lead to the City Zero
# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        roads = set()
        graph = defaultdict(set)

        for s, e in connections:
            roads.add((s, e))
            graph[s].add(e)
            graph[e].add(s)
        answer = 0
        q = deque()

        q.append((0, -1))

        while q:
            node, parent = q.popleft()
            if (parent, node) in roads:
                answer += 1

            for child in graph[node]:
                if child == parent:
                    continue
                q.append((child, node))

        return answer