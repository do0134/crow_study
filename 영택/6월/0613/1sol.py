# 백준 1244 스위치 켜고 끄기
# https://www.acmicpc.net/problem/1244

def man(idx) :
    value = idx-1
    while value < n :
        if arr[value] == 1 :
            arr[value] = 0
        else :
            arr[value] = 1
        value += idx


def girl(idx) :
    l = idx - 1
    r = idx + 1
    if arr[idx] == 1 :
        arr[idx] = 0
    else :
        arr[idx] = 1

    while 0 <= l < n and 0 <= r < n and arr[l] == arr[r] :
        if arr[l] == 0:
            arr[l] = 1
        else:
            arr[l] = 0

        if arr[r] == 0:
            arr[r] = 1
        else:
            arr[r] = 0

        l -= 1
        r += 1


n = int(input())
arr = list(map(int,input().split()))
t = int(input())

for _ in range(t) :
    gender, num = map(int,input().split())
    if gender == 1 :
        man(num)
    else :
        girl(num-1)

while len(arr) > 20 :
    print(*arr[:20])
    arr = arr[20:]
print(*arr)
