# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 일단 한 번은 무조건 쏩니다. 전부 쏴야하니까.
        # points는 무조건 하나 이상입니다.
        count = 1
        sortedArr = sorted(points)
        # 정렬된 배열의 첫번째 끝을 기준으로 잡기
        arrow = sortedArr[0][1]
        for i in range(1, len(sortedArr)):
            # 시작과 끝 잡기
            start, end = sortedArr[i]
            # 기준보다 시작이 크면
            if arrow < start:
                # 기준을 끝으로 잡고, 화살 쏘고 카운트
                arrow = end
                count += 1
            # 기준이 끝보다 크면
            elif end < arrow:
                # 기준만 끝으로 변경
                arrow = end

        return count

print(Solution().findMinArrowShots([[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]))