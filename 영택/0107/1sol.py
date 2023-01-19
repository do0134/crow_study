# leetcode 134. Gas Station
# https://leetcode.com/problems/gas-station/description/
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        dp = 0
        sum_v = 0
        answer = 0

        for i in range(n):
            temp = gas[i] - cost[i]
            sum_v += temp
            dp += temp
            if dp < 0 :
                answer = i + 1
                dp = 0

        if sum_v < 0 :
            return -1
            
        return answer