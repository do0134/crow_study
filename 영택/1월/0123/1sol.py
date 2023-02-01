# leetcode 997. Find the Town Judge
# https://leetcode.com/problems/find-the-town-judge/description/
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 :
            return 1
        judge = defaultdict(int)
        no = defaultdict(int)
        for i,j in trust :
            judge[j] += 1
            no[i] = 1

        for i,j in trust :
            if no[j] == 0 and judge[j] == n-1 :
                return j
        else :
            return -1