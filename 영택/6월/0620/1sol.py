# 백준 18429 근손실
# https://www.acmicpc.net/problem/18429

n, k = map(int,input().split())
arr = list(map(int,input().split()))
answer = 0


def solve(day, v, w):
    global answer
    if day == n:
        answer += 1
        return
    for i in range(n):
        if not v[i] and w-k+arr[i] >= 0:
            v[i] = day+1
            solve(day+1, v, w-k+arr[i])
            v[i] = 0


solve(0, [0]*n, 0)
print(answer)