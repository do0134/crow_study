# https://leetcode.com/problems/flip-string-to-monotone-increasing/
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # 0과 1 카운트를 따로 할 필요가 없었다
        m = 0
        for c in s:
            if c == '0':
                m += 1
        ans = m
        for c in s:
            if c == '0':
                m -= 1
                # 최소값으로 계속 바꿔준다!!
                # 이걸 안해서 계속 틀렸네,,
                ans = min(ans, m)
            else:
                m += 1
        return ans

print(Solution().minFlipsMonoIncr("00110"))