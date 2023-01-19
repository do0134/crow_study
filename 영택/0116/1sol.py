# leetcode 57. Insert Interval
# https://leetcode.com/problems/insert-interval/description/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        intervals.sort()
        answer = list()
        start, end = newInterval

        q = list()
        left = list()
        right = list()
        for i in intervals:
            if i[1] < start:
                left.append(i)
            elif i[0] > end:
                right.append(i)
            elif i[0] < start and i[1] > end:
                left.append(i)
            else:
                q.append(i[0])
                q.append(i[1])

        if not q:
            if not right and start > left[-1][1]:
                right.append(newInterval)
            elif not left and end < right[0][0]:
                left.append(newInterval)
            elif start > left[-1][1] and end < right[0][0]:
                left.append(newInterval)

            answer = left + right

        else:
            q.append(start)
            q.append(end)
            q.sort()
            s = q[0]
            e = q[-1]
            answer = left + [[s, e]] + right

        return answer