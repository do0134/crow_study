# leetcode 983. Minimum Cost For Tickets
# https://leetcode.com/problems/minimum-cost-for-tickets/
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        answer = int(1e9)
        q = deque()
        q.append((costs[0],days[0],0))
        q.append((costs[1],days[0]+6,0))
        q.append((costs[2],days[0]+29,0))
        n = len(days)
        dp = [int(1e9)] * 400
        while q :
            cost, day, idx = q.popleft()

            if day >= days[-1] :
                answer = min(cost, answer)
                continue
            for i in range(idx, n) :
                if days[i] > day :
                    if cost+costs[0] < dp[days[i]] and cost+costs[0] < answer:
                        q.append((cost+costs[0], days[i], i))
                        dp[days[i]] = cost+costs[0]
                    if cost+costs[1] < dp[days[i]+6] and cost+costs[1] < answer:
                        q.append((cost+costs[1], days[i]+6, i))
                        dp[days[i]+6] = cost+costs[1]
                    if cost+costs[2] < dp[days[i]+29] and cost+costs[2] < answer:
                        q.append((cost+costs[2], days[i]+29, i))
                        dp[days[i]+29] = cost+costs[2]
                    break
        return answer