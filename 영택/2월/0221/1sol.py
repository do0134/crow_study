class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for i in range(0,len(nums)-1,2) :
            if nums[i+1] != nums[i] :
                return nums[i]
        else :
            return nums[-1]
