# leetcode 1523. Count Odd Numbers in an Interval Range
# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0:
            low += 1
        if high % 2 == 0:
            high -= 1

        if low == high:
            if low % 2 == 0:
                return 0
            else:
                return 1

        value = high - low

        answer = 2 + (value - 1) // 2
        return answer