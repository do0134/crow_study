# 백준 1476 날짜 계산
# https://www.acmicpc.net/problem/1476

date = list(map(int,input().split()))
year = 0
diff = [0,0,0]
while True :
    year += 1
    for i in range(3) :
        diff[i] += 1

    if diff[0] > 15 :
        diff[0] = 1
    if diff[1] > 28 :
        diff[1] = 1
    if diff[2] > 19 :
        diff[2] = 1

    if date == diff :
        break

print(year)
