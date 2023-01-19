# leetcode 974. Subarray Sums Divisible by K
# https://leetcode.com/problems/subarray-sums-divisible-by-k/description/
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        target = 0
        answer = 0
        my_dict = defaultdict(int)
        my_dict[0] = 1
        for n in nums:
            target = (target + n) % k
            if target not in my_dict:
                my_dict[target] = 1
            else:
                answer += my_dict[target]
                my_dict[target] += 1

        return answer