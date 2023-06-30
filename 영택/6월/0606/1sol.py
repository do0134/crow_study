# 백준 18428 감시피하기
# https://www.acmicpc.net/problem/18428

n = int(input())
arr = [list(input().split()) for _ in range(n)]
flag = False

def solve(arr1, cnt, r, c):
    global flag
    if cnt == 3 :
        check(arr1)
        if flag :
            print("YES")
            exit()
        return
    for i in range(r,n) :
        if i == r and c != n-1:
            for j in range(c+1,n) :
                if arr1[i][j] == "X" :
                    arr1[i][j] = "O"
                    solve(arr1, cnt+1, i, j)
                    arr1[i][j] = "X"
        else :
            for j in range(n) :
                if arr1[i][j] == "X" :
                    arr1[i][j] = "O"
                    solve(arr1, cnt+1, i, j)
                    arr1[i][j] = "X"



def check(arr1) :
    global flag
    t = list()
    for i in range(n) :
        for j in range(n) :
            if arr1[i][j] == "T" :
                t.append((i,j))

    for r,c in t :
        r1 = r2 = r
        c1 = c2 = c
        r1 -= 1
        c1 -= 1
        r2 += 1
        c2 += 1
        while r1 >= 0 :
            if arr1[r1][c] == "O" :
                break
            elif arr1[r1][c] == "S" :
                return
            r1 -= 1
        while r2 < n :
            if arr1[r2][c] == "O" :
                break
            elif arr1[r2][c] == "S" :
                return
            r2 += 1
        while c1 >= 0:
            if arr1[r][c1] == "O":
                break
            elif arr1[r][c1] == "S":
                return
            c1 -= 1
        while c2 < n:
            if arr1[r][c2] == "O":
                break
            elif arr1[r][c2] == "S":
                return
            c2 += 1
    else :
        flag = True


for i in range(n) :
    for j in range(n) :
        if arr[i][j] == "X" :
            arr[i][j] = "O"
            solve(arr,1,i,j)
            arr[i][j] = "X"
print("NO")