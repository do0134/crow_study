# 프로그래머스 코딩 테스트 공부
# https://school.programmers.co.kr/learn/courses/30/lessons/118668
def solution(alp, cop, problems):
    max_a = alp
    max_c = cop
    for problem in problems:
        max_a = max(problem[0], max_a)
        max_c = max(problem[1], max_c)

    dp = [[int(1e9)] * (max_c + 1) for _ in range(max_a + 1)]
    dp[alp][cop] = 0

    for a in range(alp, max_a + 1):
        for c in range(cop, max_c + 1):
            if a + 1 <= max_a:
                dp[a + 1][c] = min(dp[a][c] + 1, dp[a + 1][c])
            if c + 1 <= max_c:
                dp[a][c + 1] = min(dp[a][c] + 1, dp[a][c + 1])
            for problem in problems:
                if problem[0] <= a and problem[1] <= c:
                    next_a = min(max_a, a + problem[2])
                    next_c = min(max_c, c + problem[3])
                    dp[next_a][next_c] = min(dp[next_a][next_c], dp[a][c] + problem[4])

    return dp[-1][-1]