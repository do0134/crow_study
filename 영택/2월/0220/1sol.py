class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s, e = 0, len(nums) - 1

        while s <= e:
            mid = (s + e) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                e = mid - 1
            elif nums[mid] < target:
                s = mid + 1

        if nums[mid] > target:
            return mid
        else:
            return mid + 1

