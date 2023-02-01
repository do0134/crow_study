# leetcode 1626. Best Team With No Conflicts
# https://leetcode.com/problems/best-team-with-no-conflicts/description/
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        teammate = sorted([[ages[i], scores[i]] for i in range(n)])
        dp = [0] * n

        for i in range(n):
            dp[i] = teammate[i][1]
            for j in range(i - 1, -1, -1):
                if teammate[i][1] >= teammate[j][1]:
                    dp[i] = max(dp[i], dp[j] + teammate[i][1])

        return max(dp)