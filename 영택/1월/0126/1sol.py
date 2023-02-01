# leetcode 787. Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [int(1e9)] * n
        airport = [[0] * n for _ in range(n)]
        for i, j, p in flights:
            airport[i][j] = p

        q = deque()
        q.append((src, 0, -1))
        dp[src] = 0
        answer = int(1e9)

        while q:
            c_place, c_cost, c_move = q.popleft()
            if c_move > k:
                continue
            else:
                if c_place == dst and c_cost < answer:
                    answer = c_cost

                for n_place, n_cost in enumerate(airport[c_place]):
                    if n_cost != 0 and dp[n_place] > n_cost + c_cost:
                        q.append((n_place, c_cost + n_cost, c_move + 1))
                        dp[n_place] = n_cost + c_cost

        if answer == int(1e9):
            return -1
        else:
            return answer