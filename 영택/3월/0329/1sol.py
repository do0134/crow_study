# leetcode 1402. Reducing Dishes
# https://leetcode.com/problems/reducing-dishes/description/

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        satisfaction.sort(reverse = True)
        answer, temp = 0, 0
        for i in range(n) :
            temp += satisfaction[i]
            if temp < 0 :
                break
            answer += temp
        return answer