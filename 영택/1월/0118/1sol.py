# leetcode 918. Maximum Sum Circular Subarray
# https://leetcode.com/problems/maximum-sum-circular-subarray/description/

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        a_max = a_min = idx_max = idx_min = nums[0]

        for i in nums[1:]:
            idx_max = max(idx_max + i, i)
            idx_min = min(idx_min + i, i)
            a_max = max(a_max, idx_max)
            a_min = min(idx_min, a_min)

        if sum(nums) != a_min:
            return max(sum(nums) - a_min, a_max)
        else:
            return a_max