# https://leetcode.com/problems/maximum-sum-circular-subarray/
from typing import List

class Solution:
    # 연속된 인덱스를 가진 부분 배열 중 가장 큰 합 구하기
    # 요새 모르겠어서 계속 답을 봅니다. 슬픔.
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # 이거랑 minNum의 기능을 잘 모르겠습니다
        sumNum = sum(nums)
        maxSum = nums[0]
        curMax = nums[0]
        minNum = 0
        for i in range(1, len(nums)):
            curMax = max(curMax + nums[i], nums[i])
            minNum = min(minNum + nums[i], nums[i])
            maxSum = max(maxSum, curMax, sumNum - minNum)
        return maxSum

print(Solution().maxSubarraySumCircular([1,-2,3,-2]))