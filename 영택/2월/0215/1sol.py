# leetcode 989. Add to Array-Form of Integer
# https://leetcode.com/problems/add-to-array-form-of-integer/description/
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = ""
        for i in num:
            n += str(i)

        answer_num = str(int(n) + k)
        answer = list()
        for i in answer_num:
            answer.append(int(i))
        return answer
