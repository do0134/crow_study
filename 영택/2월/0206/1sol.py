# leetcode 1470. Shuffle the Array
# https://leetcode.com/problems/shuffle-the-array/description/
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer = list()
        for a, b in zip(nums[:n], nums[n:]):
            answer.append(a)
            answer.append(b)

        return answer