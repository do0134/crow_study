# leetcode 881. Boats to Save People
# https://leetcode.com/problems/boats-to-save-people/description/
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        answer = idx = 0
        r = len(people) - 1
        while idx <= r:
            if people[idx] + people[r] <= limit:
                idx += 1
                r -= 1
            else:
                r -= 1
            answer += 1

        return answer