# leetcode 438. Find All Anagrams in a String
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        cnt, m = Counter(p), len(p)
        answer = list()
        if n < m:
            return answer

        temp = Counter(s[:m])
        for i in temp:
            if i in cnt:
                cnt[i] -= temp[i]

        if all([cnt[i] == 0 for i in cnt]):
            answer.append(0)

        for i in range(1, n - m + 1):
            if s[i - 1] in cnt:
                cnt[s[i - 1]] += 1
            if s[i + m - 1] in cnt:
                cnt[s[i + m - 1]] -= 1
            if all([cnt[j] == 0 for j in cnt]):
                answer.append(i)

        return answer