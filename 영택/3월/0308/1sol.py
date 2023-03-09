# 백준  소트
# https://www.acmicpc.net/problem/1083
n = int(input())
arr = list(map(int,input().split()))
s = int(input())

def solve() :
    global arr, s, n
    idx = 0
    target = sorted(arr, reverse=True)
    while idx <= n-1 :
        if arr == target or s == 0 :
            return arr

        if n-1 < idx+s :
            temp = arr[idx : n]
        else :
            temp = arr[idx : idx+s+1]

        max_v = max(temp)
        max_idx = arr.index(max_v)

        for i in range(max_idx,0,-1) :
            if arr[i] > arr[i-1] :
                arr[i],arr[i-1] = arr[i-1],arr[i]
                s -= 1
                if s == 0 :
                    return arr
        idx += 1




print(*solve())

