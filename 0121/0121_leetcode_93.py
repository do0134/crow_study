# https://leetcode.com/problems/restore-ip-addresses/
from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        answer = []
        # 현재 방문 중인 위치, 이전에 모은 주소
        def backTracking(i, address):
            # 더 돌 숫자가 없을 때
            if i == len(s):
                if len(address) == 4:
                    answer.append(".".join(map(str, address)))
                return

            # 마지막 주소가 0이 아니고 연결된 주소가 255 이하
            if address[-1] != 0 and address[-1] * 10 + int(s[i]) <= 255:
                lastItem = address[-1]
                # 현재 상태를 인접 상태로 바꾸기
                address[-1] = lastItem * 10 + int(s[i])
                # 재귀
                backTracking(i + 1, address)
                # 상태 복원
                address[-1] = lastItem

            # 주소에 4개 미만의 숫자가 들어갈 경우
            if len(address) < 4:
                # 현재 상태를 인접 상태로 바꾸기
                address.append(int(s[i]))
                # 재귀
                backTracking(i + 1, address)
                # 상태 복원
                address.pop()

        backTracking(1, [int(s[0])])
        return answer

print(Solution().restoreIpAddresses("25525511135"))