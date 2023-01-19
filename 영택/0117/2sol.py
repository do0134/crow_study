# leetcode 926. Flip String to Monotone Increasing
# https://leetcode.com/problems/flip-string-to-monotone-increasing/description/

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        z_cnt = s.count("0")
        if z_cnt == n or z_cnt == 0 :
            return 0
        o_cnt = 0
        answer = z_cnt

        for i in s :
            if i == "0" :
                z_cnt -= 1
            else :
                o_cnt += 1
            answer = min(answer, z_cnt+o_cnt)
        return answer
