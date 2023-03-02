# leetcode 443. String Compression
# https://leetcode.com/problems/string-compression/description/
class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n == 1:
            return n

        answer = 0
        for i in range(n):
            if not chars[i]:
                continue
            if i < answer:
                continue
            if i < n - 1 and chars[i] != chars[i + 1]:
                chars[answer] = chars[i]
                answer += 1
            elif i == n - 1 and chars[i]:
                chars[answer] = chars[i]
                answer += 1
            elif chars[i] == chars[i + 1]:
                chars[answer] = chars[i]

                answer += 1
                idx = i + 1
                cnt = 1
                while idx <= n - 1 and chars[i] == chars[idx]:
                    chars[idx] = ""
                    idx += 1
                    cnt += 1

                for s in str(cnt):
                    chars[answer] = s
                    answer += 1

        return answer
