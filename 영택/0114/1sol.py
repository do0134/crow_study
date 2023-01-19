# leetcode 1061. Lexicographically Smallest Equivalent String
# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/description/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        str_dict = defaultdict(set)

        for i in range(len(s1)):
            str_dict[s1[i]].add(s2[i])
            str_dict[s2[i]].add(s1[i])

        def dfs(s, m, v):
            v.append(s)
            temp = m
            for i in str_dict[s]:
                if i not in v:
                    temp = min(temp, dfs(i, min(temp, i), v))
            return temp

        answer = ""

        for i in baseStr:
            answer += dfs(i, i, [])
        return answer