from typing import List

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = 0
        countList = {}
        # 딕셔너리에 담기
        for i in tasks:
            try:
                # 이미 존재하는 값이면 value 카운트 추가
                countList[i] += 1
            except:
                # 처음 들어오면 value 1
                countList[i] = 1
        # 판별식
        for value in countList.values():
            a = value // 3 - 1
            b = value - (3 * a)
            if value == 1:
                count = -1
                break
            # 2보다 크고 3의 배수일 때
            elif value >= 2 and value % 3 == 0:
                count += value // 3
            # 2보다 크고 3의 배수 아니고 2의 배수일 때
            elif 2 <= value <= 4 and value % 2 == 0:
                count += value // 2
            # 2보다 크고 3으로 나눠지고 나머지가 4 이하의 짝수일 때
            elif value >= 2 and value // 3 and 2 <= (value % 3) <= 4:
                count += value // 3
                if 2 <= (value % 3) <= 4:
                    count += (value % 3) // 2
            # 2보다 크고 3으로 나눠지고 나머지가 1인데 3으로 한 번 덜 나누면 나머지가 4 이하의 짝수일 때
            elif value >= 2 and value // 3 and value % 3 == 1 and 2 <= b <= 4:
                count += a
                if 2 <= b <= 4:
                    count += b // 2

        return count
    # value % 3 == 1인 경우는 value // 3 + 2
    # value % 3 == 2인 경우는 value // 3 + 1
    # 이 되는 패턴이 존재한다. 저렇게 지저분하게 계산할 필요가 없었다!

tasks = [119,115,115,119,118,113,118,120,110,113,119,115,116,118,120,117,116,111,113,119,115,113,115,111,112,119,111,111,110,112,113,120,110,111,112,111,119,112,113,112,115,116,113,114,118,119,115,114,114,112,110,117,120,110,117,116,120,118,110,120,119,113,119,120,113,110,120,114,119,115,119,117,120,116,113,113,110,118,117,116,114,114,111,116,119,112,113,116,112,116,119,112,114,114,112,118,116,113,117,116]
print(Solution().minimumRounds(tasks))