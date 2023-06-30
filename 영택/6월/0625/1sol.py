# 백준 1251 단어 나누기
# https://www.acmicpc.net/problem/1251

a = list(input())
answer_list = list()

def solve(s1,s2,s3):
    global answer_list
    temp_list = s1[::-1] + s2[::-1] + s3[::-1]
    temp = ("").join(temp_list)
    answer_list.append(temp)

for i in range(len(a)-2):
    for j in range(i+1,len(a)-1):
        solve(a[:i+1],a[i+1:j+1],a[j+1:])

answer_list.sort()
print(answer_list[0])
