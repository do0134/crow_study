# leetcode 1345. Jump Game IV
# https://leetcode.com/problems/jump-game-iv/description/
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        answer = int(1e9)
        if n == 1:
            return 0

        num = defaultdict(list)
        for i in range(n):
            num[arr[i]].append(i)

        q = deque()
        v = [int(1e9)] * n
        v_num = set()
        q.append((0, 0))
        while q:
            idx, cnt = q.popleft()
            if idx == n - 1:
                answer = min(cnt, answer)
            else:
                if v[idx + 1] > cnt + 1:
                    v[idx + 1] = cnt + 1
                    q.append((idx + 1, cnt + 1))
                if idx != 0 and v[idx - 1] > cnt + 1:
                    v[idx - 1] = cnt + 1
                    q.append((idx - 1, cnt + 1))
                if arr[idx] not in v_num:
                    for i in num[arr[idx]]:
                        if v[i] > cnt + 1:
                            v[i] = cnt + 1
                            q.append((i, cnt + 1))
                    v_num.add(arr[idx])

        return answer 