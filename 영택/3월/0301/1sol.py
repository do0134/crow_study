# leetcode 912. Sort an Array
# https://leetcode.com/problems/sort-an-array/description/
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        answer = list()
        cnt, min_v, max_v = Counter(nums), min(nums), max(nums)
        for idx in range(min_v, max_v+1) :
            answer.extend([idx]*cnt[idx])

        return answer