# leetcode 904. Fruit Into Baskets
# https://leetcode.com/problems/fruit-into-baskets/description/
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) <= 2:
            return len(fruits)

        answer = 0
        l = [fruits[0], 1]
        r = [-1, 0]

        for i in range(1, len(fruits)):
            if r[0] == -1:
                if fruits[i] != l[0]:
                    r[0] = fruits[i]
                    r[1] += 1
                else:
                    l[1] += 1
            else:
                if fruits[i] != r[0] and fruits[i] != l[0]:
                    l = [fruits[i - 1], 0]
                    r = [fruits[i], 1]
                    for j in range(i - 1, -1, -1):
                        if fruits[j] != l[0]:
                            break
                        l[1] += 1
                elif fruits[i] != r[0]:
                    l[1] += 1
                else:
                    r[1] += 1

            if l[1] + r[1] > answer:
                answer = l[1] + r[1]

        return answer