# 백준 10830 행렬제곱
# https://www.acmicpc.net/problem/10830

import sys

n, b = map(int,sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]


def square(arr1, arr2) :
    value = [[0]*n for _ in range(n)]
    for r in range(n) :
        for c in range(n) :
            for i in range(n) :
                value[r][c] += arr1[r][i] * arr2[i][c]
                value[r][c] %= 1000

    return value


def dq(arr1, num) :
    if num == 1 :
        for i in range(n) :
            for j in range(n) :
                arr1[i][j] %= 1000
        return arr1

    dq1 = dq(arr1, num//2)

    if num % 2 :
        return square(square(dq1,dq1), arr1)
    else :
        return square(dq1,dq1)


answer = dq(arr,b)

for i in answer :
    print(*i)