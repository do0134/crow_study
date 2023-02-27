# leetcode 502. IPO
# https://leetcode.com/problems/ipo/description/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pc = sorted(zip(profits, capital), key=lambda x: x[1])
        heap = list()
        i = 0
        for _ in range(k):
            while i < len(pc) and w >= pc[i][1]:
                heapq.heappush(heap, -pc[i][0])
                i += 1
            if heap:
                w -= heapq.heappop(heap)

        return w
