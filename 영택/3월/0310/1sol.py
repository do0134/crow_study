idx = 1
n_1 = 0
n_2 = 1
n = int(input())

while idx < n :
    next = n_1 + n_2
    n_1 = n_2
    n_2 = next
    idx += 1
if n == 0 :
    print(0)
else :
    print(n_2)
