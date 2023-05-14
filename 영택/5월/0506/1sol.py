# 백준 1038 줄어드는 수
# https://www.acmicpc.net/problem/1174

n = int(input())
my_dict = {}
for i in range(1,11) :
    my_dict[i] = set()

for i in range(10) :
    my_dict[1].add(i)
def solve(idx) :
    if idx == 10 :
        return
    for i in my_dict[idx] :
        i = str(i)
        for j in range(int(i[0])+1,10) :
            num = str(j)+i
            my_dict[idx+1].add(num)
    solve(idx+1)

solve(1)
answer = list()
for i in range(1,11) :
    for j in my_dict[i] :
        answer.append(int(j))

if len(answer) < n :
    print(-1)
else :
    answer.sort()
    print(answer[n-1])