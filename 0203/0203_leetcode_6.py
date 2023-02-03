# https://leetcode.com/problems/zigzag-conversion/
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s and numRows <= 0:
            return ""
        elif numRows == 1:
            return s
        answer = ""
        # 띄워 읽기 패턴
        count = 2 * numRows - 2
        for i in range(0, numRows):
            for j in range(i, len(s), count):
                answer += s[j]
                # 두 번째 줄의 두 번째 인자부터 띄워 읽기 패턴 바뀜
                if i != 0 and i != numRows - 1 and (j + count -2 * i) < len(s):
                    answer += s[j + count - 2 * i]
        return answer

print(Solution.convert("PAYPALISHIRING", 3))