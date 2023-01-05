# leetcode 452. Minimum Number of Arrows to Burst Balloons
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x : x[1])
        answer = 1
        point = points[0][1]
        for i in points :
            if point < i[0] :
                point = i[1]
                answer += 1
        return answer