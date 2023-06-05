# 백준 2661 좋은수열
# https://www.acmicpc.net/problem/2661

n = int(input())


def solve(num) :
    if len(num) == n :
        print(num)
        exit()

    for i in "123" :
        temp = num + i
        if check(temp) :
            solve(temp)


def check(num) :
    for i in range(1, len(num)//2+1) :
        if num[-i:] == num[-i*2:-i] :
            return False

    return True


solve("1")