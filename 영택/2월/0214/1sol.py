# leetcode 67. Add Binary
# https://leetcode.com/problems/add-binary/description/
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        an = int(a, 2)
        bn = int(b, 2)

        cn = an + bn

        return format(cn, "b")