# leetcode 567. Permutation in String
# https://leetcode.com/problems/permutation-in-string/description/
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt, l = Counter(s1), len(s1)

        for i in range(len(s2)):
            if s2[i] in cnt:
                cnt[s2[i]] -= 1
            if i >= l and s2[i - l] in cnt:
                cnt[s2[i - l]] += 1
            if all([cnt[i] == 0 for i in cnt]):
                return True

        return False