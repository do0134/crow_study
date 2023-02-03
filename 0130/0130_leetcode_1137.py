# https://leetcode.com/problems/n-th-tribonacci-number/
# The Tribonacci sequence Tn is defined as follows:
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, return the value of Tn.
# 문제 2번째 줄(조건)을 만족하는 식을 만들면 된다.
# 트리보나치 수열에 대한 설명은 다음을 참고했다.
    # https://zzonglove.tistory.com/39
class Solution:
    def tribonacci(self, n: int) -> int:
        zero = 0
        one = 1
        two = 1
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        for i in range(3, n + 1):
            three = zero + one + two
            zero = one
            one = two
            two = three
        return three

print(Solution().tribonacci(25))