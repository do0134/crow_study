# leetcode 64. Minimum Path Sum
# https://leetcode.com/problems/minimum-path-sum/description/
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[int(1e9)] * m for _ in range(n)]

        q = deque()
        q.append((0, 0))
        dp[0][0] = grid[0][0]

        while q:
            cr, cc = q.popleft()
            for dr, dc in ((1, 0), (0, 1)):
                nr = dr + cr
                nc = dc + cc
                if 0 <= nr < n and 0 <= nc < m and dp[nr][nc] > dp[cr][cc] + grid[nr][nc]:
                    q.append((nr, nc))
                    dp[nr][nc] = dp[cr][cc] + grid[nr][nc]

        return dp[n - 1][m - 1]
