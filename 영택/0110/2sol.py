# 백준 단축키 지정
# https://www.acmicpc.net/problem/1283
from collections import defaultdict
n = int(input())

my_dict = defaultdict(str)

for _ in range(n) :
    temp = input()
    idx = 0
    temp1 = temp.split()
    flag = False
    if not my_dict[temp[0].upper()] :
        my_dict[temp[0].upper()] = temp
        flag = True

    elif my_dict[temp[0].upper()] :
        for p in range(len(temp1)) :
            if not my_dict[temp1[p][0].upper()] :
                my_dict[temp1[p][0].upper()] = temp
                idx = temp.index(temp1[p])
                flag = True
                break

    if not flag :
        for i in range(len(temp)) :
            if temp[i] == " " :
                continue
            if not my_dict[temp[i].upper()] :
                my_dict[temp[i].upper()] = temp
                idx = i
                flag = True
                break
    answer = ""
    for j in range(len(temp)) :
        if flag and j == idx :
            answer += f"[{temp[j]}]"
        else :
            answer += temp[j]
    print(answer)
