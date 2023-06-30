# 백준 2632 피자판매
# https://www.acmicpc.net/problem/2632

from collections import defaultdict


def make_pre(target, pre_dict):
    global p
    l = len(target)
    for i in range(l):
        value = target[i]
        pre_dict[value] += 1
        for j in range(i+1,l):
            value += target[j]
            pre_dict[value] += 1
            if value > p:
                break

        for k in range(i-1):
            value += target[k]
            if value > p:
                break
            pre_dict[value] += 1

p = int(input())
n, m = map(int,input().split())
a = list()
b = list()

for _ in range(n):
    a.append(int(input()))

for _ in range(m):
    b.append(int(input()))

a_dict = defaultdict(int)
b_dict = defaultdict(int)
a_dict[0] = b_dict[0] = 1

make_pre(a, a_dict)
make_pre(b, b_dict)

answer = 0


for i in range(p+1):
    answer += a_dict[i] * b_dict[p-i]

print(answer)
