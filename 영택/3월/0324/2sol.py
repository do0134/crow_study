# 프로그래머스 택배 배달과 수거하기
# https://school.programmers.co.kr/learn/courses/30/lessons/150369
def solution(cap, n, d, p):
    answer = 0
    dp = [[0, 0] for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        c_d, c_p = d[i], p[i]
        dp[i][0] = dp[i + 1][0] - c_d
        dp[i][1] = dp[i + 1][1] - c_p

        if dp[i][0] < 0 or dp[i][1] < 0:
            move = (i + 1) * 2
            cnt = 0
            while dp[i][0] < 0 or dp[i][1] < 0:
                dp[i][0] += cap
                dp[i][1] += cap
                cnt += 1
            answer += cnt * move

    return answer