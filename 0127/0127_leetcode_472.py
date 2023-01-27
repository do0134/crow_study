# https://leetcode.com/problems/concatenated-words/
from typing import List

class Solution:
    # 연결된 단어 찾기
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # 무슨 소린지 모르겠어서 참고함
        # 둘 혹은 그 이상의 단어 리스트
        def can(w, dit):  # w가 확인할 단어, dit이 단어 리스트
            for i in range(mini, len(w)):
                lf = w[:i]  # left first? 단어 앞에서부터 확인
                rt = w[i:]  # right tale? 단어 뒤에서부터 확인
                # set에 단어 반짝이 있다면?? 을 판단
                if lf in dit:
                    if rt in dit or can(rt, dit):
                        return True
            return False

        res = []
        # set으로 만들어버렸다! 와!
        dit = set(list(words))
        mini = 10000
        for w in words:
            mini = min(len(w), mini)
        for w in words:
            if can(w, dit):
                res.append(w)

        return res
print(Solution().findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))