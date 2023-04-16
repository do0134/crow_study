# 704. Binary Search
# https://leetcode.com/problems/binary-search/description/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums)

        while s < e :
            mid = (s+e) // 2
            if nums[mid] == target :
                return mid
            if nums[mid] > target :
                e = mid
            elif nums[mid] < target :
                s = mid+1
        return -1