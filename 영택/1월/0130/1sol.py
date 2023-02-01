# leetcode 1137. N-th Tribonacci Number
# https://leetcode.com/problems/n-th-tribonacci-number/description/
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        trib = [0] * 38
        trib[0] = 0
        trib[1] = trib[2] = 1
        for i in range(3, n + 1):
            trib[i] = trib[i - 1] + trib[i - 2] + trib[i - 3]

        return trib[n]