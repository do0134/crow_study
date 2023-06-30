# 백준 17609 회문
# https://www.acmicpc.net/problem/17609

def solve(s):
    l, r = 0 , len(s)-1
    cnt = 0
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        elif s[l] != s[r]:
            l_i, r_j = int(1e9), int(1e9)
            if l+1 <= r and s[l+1] == s[r]:
                l_i = solve(s[l+1:r+1])

            if r-1 >= l and s[r-1] == s[l]:
                r_j = solve(s[l:r])


            if min(l_i,r_j) > 2:
                return 2
            else:
                cnt += min(l_i,r_j) + 1
            if cnt > 1:
                return 2
            if l_i < r_j :
                l += 1
            else:
                r -= 1
    else:
        if cnt:
            return 1
        else:
            return 0


t = int(input())

for _ in range(t):
    target = input()
    print(solve(target))
