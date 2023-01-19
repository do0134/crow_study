# leetcode 2244. Minimum Rounds to Complete All Tasks
# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        a = Counter(tasks)
        answer = 0
        for i,j in a.items() :
            if a[i] <= 1 :
                return -1
            
            answer += ceil(j/3)

        return answer