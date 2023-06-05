# 백준 10655 마라톤1
# https://www.acmicpc.net/problem/10655

n = int(input())
arr = list()
value = 0

for _ in range(n) :
    temp = list(map(int,input().split()))
    if _ != 0 :
        value += abs(arr[-1][0]-temp[0]) + abs(arr[-1][1]-temp[1])
    arr.append(temp)

answer = value
for i in range(1,n-1) :
    temp = value
    temp -= abs(arr[i-1][0] - arr[i][0]) + abs(arr[i-1][1] - arr[i][1]) + abs(arr[i][0] - arr[i+1][0]) + abs(arr[i][1] - arr[i+1][1])
    temp += abs(arr[i-1][0] - arr[i+1][0]) + abs(arr[i-1][1] - arr[i+1][1])
    answer = min(answer, temp)

print(answer)
