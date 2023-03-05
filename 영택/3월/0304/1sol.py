# leetcode 2444. Count Subarrays With Fixed Bounds
# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/description/
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        min_idx = max_idx = -1
        idx = 0
        answer = 0

        for i, value in enumerate(nums):
            if value < minK or value > maxK:
                idx = i + 1
            else:
                if value == minK:
                    min_idx = i
                if value == maxK:
                    max_idx = i
                if min_idx >= idx and max_idx >= idx:
                    answer += min(min_idx, max_idx) - idx + 1

        return answer
