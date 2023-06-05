# 백준 16637 괄호 추가하기
# https://www.acmicpc.net/problem/16637

n = int(input())
arr = list(input())

for i in range(0,n,2) :
    arr[i] = int(arr[i])

answer = -int(1e9)


def calc(arr1, length) :
    global answer
    if len(arr1) == 1 :
        answer = max(answer, arr1[0])
        return

    for i in range(1, min(len(arr1), length),2) :
        if arr1[i] == "+" :
            temp = arr1[i-1] + arr1[i+1]
        elif arr1[i] == "*" :
            temp = arr1[i-1] * arr1[i+1]
        else :
            temp = arr1[i-1] - arr1[i+1]
        if i == 1 :
            l = 4
        else :
            l = 2
        calc(arr1[:i-1] + [temp] + arr1[i+2:], l)



calc(arr, min(n,4))
print(answer)