# leetcode 131. Palindrome Partitioning
# https://leetcode.com/problems/palindrome-partitioning/description/
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = list()

        def check(string):
            if len(string) == 1:
                return True
            for i in range(len(string) // 2 + 1):
                if string[i] != string[-(i + 1)]:
                    return False
            return True

        def back_tracking(o, v, answer):
            n = len(o)
            if n == 0:
                answer.append(v)
                return
            else:
                for i in range(1, n + 1):
                    if check(o[:i]):
                        back_tracking(o[i:], v + [o[:i]], answer)

        back_tracking(s, [], answer)
        return answer