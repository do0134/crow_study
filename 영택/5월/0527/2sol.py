# 백준 12919 A와 B 2
# https://www.acmicpc.net/problem/12919s

def make(s, t) :
    global flag
    if len(s) == len(t) :
        if s == t :
            flag = 1
        return
    if t[-1] == "A" :
        make(s,t[:len(t)-1])
    if t[0] == "B" :
        temp = t[1:]
        make(s,temp[::-1])

S = input()
T = input()
flag = 0
make(S, T)
print(flag)
