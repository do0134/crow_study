# leetcode 6. Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion/description/
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 :
            return s
        zigzag = [[] for _ in range(numRows)]
        answer = ""
        r = c = 0

        for i in s :
            while c != len(zigzag[r])-1 :
                zigzag[r].append("")
            zigzag[r].append(i)
            if c == 0 or c%(numRows-1) == 0 :
                if r != numRows-1 :
                    r += 1
                else :
                    r -= 1
                    c += 1
            else :
                r -= 1
                c += 1

        for i in zigzag :
            for s in i :
                if s == "" :
                    continue
                else :
                    answer += s
        return answer