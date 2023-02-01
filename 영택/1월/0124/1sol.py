# leetcode 909. Snakes and Ladders
# https://leetcode.com/problems/snakes-and-ladders/description/
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        v = [int(1e9)] * (n ** 2 + 1)
        arr = [0]
        idx = 1
        for i in range(n - 1, -1, -1):
            for j in range(n):
                if (n - i) % 2 == 1:
                    if board[i][j] != -1:
                        arr.append(board[i][j])
                        idx += 1
                    else:
                        arr.append(idx)
                        idx += 1
                else:
                    if board[i][n - j - 1] != -1:
                        arr.append(board[i][n - j - 1])
                        idx += 1
                    else:
                        arr.append(idx)
                        idx += 1
        q = deque()
        q.append((1, 0))
        v[1] = 0
        while q:
            cl, move = q.popleft()

            for i in range(cl + 1, min(n ** 2 + 1, cl + 7)):
                if v[arr[i]] > move + 1:
                    q.append((arr[i], move + 1))
                    v[arr[i]] = move + 1

        if v[n ** 2] == int(1e9):
            return -1
        else:
            return v[n ** 2]