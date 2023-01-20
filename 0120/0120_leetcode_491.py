# https://leetcode.com/problems/non-decreasing-subsequences/
from typing import List
from itertools import combinations
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # 감소하지 않는 => 증가하는 부분 수열 구하기
        answer = []
        for i in range(1, len(nums)):
            temp = []
            comb = combinations(nums, i)
            for j in comb:
                if 1 < len(j) and list(j) not in answer and sorted(list(j)) == list(j):
                    answer.append(list(j))
        if 1 < len(nums) and nums not in answer and sorted(nums) == nums:
            answer.append(nums)
        answer.sort()
        return answer

print(Solution().findSubsequences([4,6,7,7]))
