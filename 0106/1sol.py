# leetcode 1833. Maximum Ice Cream Bars
# https://leetcode.com/problems/maximum-ice-cream-bars/description/
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        idx = 0
        answer = 0
        while coins > 0 and idx < len(costs) :
            if costs[idx] > coins : 
                break
            
            coins -= costs[idx]
            idx += 1
            answer += 1
            
            if idx == len(costs) :
                break

        return answer