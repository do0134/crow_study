# 백준 11723 집합
# https://www.acmicpc.net/problem/11723

from collections import defaultdict
import sys

class Solve:
    def __init__(self):
        self.data = defaultdict(int)

    def add(self, idx):
        self.data[idx] = 1

    def remove(self, idx):
        self.data[idx] = 0

    def check(self, idx):
        print(self.data[idx])

    def toggle(self, idx):
        if self.data[idx] :
            self.data[idx] = 0
        else :
            self.data[idx] = 1

    def all(self):
        for i in range(1,21) :
            self.data[i] = 1

    def empty(self):
        for i in range(1,21) :
            self.data[i] = 0


n = int(input())
s = Solve()

for _ in range(n) :
    a = list(sys.stdin.readline().split())
    if a[0] == "all" :
        s.all()
    elif a[0] == "empty" :
        s.empty()
    elif a[0] == "add" :
        s.add(int(a[1]))
    elif a[0] == "remove" :
        s.remove(int(a[1]))
    elif a[0] == "check" :
        s.check(int(a[1]))
    elif a[0] == "toggle" :
        s.toggle(int(a[1]))