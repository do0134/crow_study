# leetcode 2348. Number of Zero-Filled Subarrays
# https://leetcode.com/problems/number-of-zero-filled-subarrays/description/
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        idx = 0
        answer = 0
        cnt = 0
        while idx < len(nums):
            if nums[idx]:
                cnt = 0
                idx += 1
            else:
                cnt += 1
                idx += 1
                answer += cnt

        return answer