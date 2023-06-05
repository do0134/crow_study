# 백준 2668 숫자고르기
# https://www.acmicpc.net/problem/2668

n = int(input())
my_dict = {}

for i in range(1,n+1) :
    my_dict[i] = int(input())

answer = set()
stack = list()


for i in range(1,n+1) :
    parent = set()
    child = set()
    v = [0] * (n+1)
    if i not in answer :
        stack.append(i)
        parent.add(i)
        v[i] = 1
        while stack :
            idx = stack.pop()
            child.add(my_dict[idx])
            parent.add(idx)

            if not v[my_dict[idx]] :
                stack.append(my_dict[idx])
                v[my_dict[idx]] = 1
            if parent == child :
                for j in parent :
                    answer.add(j)
                parent = set()
                child = set()



answer = sorted(list(answer))
print(len(answer))
for i in answer :
    print(i)
