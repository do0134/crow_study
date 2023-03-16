# 백준 짐 챙기는 숌
# https://www.acmicpc.net/problem/1817

n,m = map(int,input().split())

def solve() :
    if n == 0 :
        return 0
    books  = list(map(int,input().split()))
    idx = 0
    answer = 0
    while idx < n :
        temp = 0
        for i in range(idx, n) :
            if temp + books[i] > m :
                answer += 1
                idx = i
                break
            else :
                temp += books[i]
                if i == n-1 :
                    idx = n
                    answer += 1
                    break

    return answer

print(solve())