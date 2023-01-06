# https://leetcode.com/problems/maximum-ice-cream-bars/
from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        sortedCosts = sorted(costs)
        count = 0
        for i in range(len(sortedCosts)):
            if sortedCosts[0] > coins:
                break
            elif (coins - sortedCosts[i]) >= 0:
                coins -= sortedCosts[i]
                count += 1
            else:
                break
        return count

print(Solution().maxIceCream([1,3,2,4,1], 7))
