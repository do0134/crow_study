# https://leetcode.com/problems/insert-interval/
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        answer = []
        for i in range(len(intervals)):
            # 새 인터벌이 작을 때
            if newInterval[1] < intervals[i][0]:
                answer.append(newInterval)
                return answer + intervals[i:]
            # 새 인터벌이 더 클 때
            elif intervals[i][1] < newInterval[0]:
                answer.append(intervals[i])
            # 나머지
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        # 작을 때 빼고
        answer.append(newInterval)
        return answer

print(Solution().insert([[1,3],[6,9]], [2,5]))