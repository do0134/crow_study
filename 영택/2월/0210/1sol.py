# leetcode 1162. As Far from Land as Possible
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]
        q = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))

        if len(q) == n ** 2 or len(q) == 0:
            return -1

        answer = 0

        while q:
            cn = len(q)
            for _ in range(cn):
                cr, cc = q.popleft()
                for d in range(4):
                    nr, nc = dr[d] + cr, dc[d] + cc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        q.append((nr, nc))
                        grid[nr][nc] = 1

            answer += 1

        return answer - 1
