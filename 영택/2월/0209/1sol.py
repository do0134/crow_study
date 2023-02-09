# leetcode 2306. Naming a Company
# https://leetcode.com/problems/naming-a-company/description/
class Solution:
    def distinctNames(self, A: List[str]) -> int:
        m, ans, A = defaultdict(lambda: defaultdict(int)), 0, set(A)
        for w in A:
            for x in ascii_lowercase:
                if x + w[1:] not in A: m[x][w[0]] += 1
        for w in A:
            for x in ascii_lowercase:
                if x + w[1:] not in A: ans += m[w[0]][x]
        return ans
