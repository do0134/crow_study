# leetcode 2300. Successful Pairs of Spells and Potions
# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(spells)
        m = len(potions)
        answer = list()
        potions.sort()

        for spell in spells:
            s = 0
            e = m
            while s < e:
                mid = (s + e) // 2
                if spell * potions[mid] >= success:
                    e = mid
                else:
                    s = mid + 1
            answer.append(m - e)

        return answer