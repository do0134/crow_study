# 백준 1789 수들의 합
# https://www.acmicpc.net/problem/1789

s = int(input())
temp = 0
answer = 0
for i in range(1,s+1):
    temp += i
    answer += 1
    if temp+i+1>s:
        break
print(answer)