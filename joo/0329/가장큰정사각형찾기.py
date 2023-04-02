# programmers 연습 문제 - 가장 큰 정사각형 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/12905

def solution(board):
    dp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    maxx = 0
    for i in range(1, len(board) + 1):
        for j in range(1, len(board[0]) + 1):
            if board[i-1][j-1] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                if dp[i][j] > maxx:
                    maxx = dp[i][j]
    return maxx ** 2




b1 = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]
b2 = [[0, 0, 1, 1], [1, 1, 1, 1]]
b3 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
print(solution(b2))
