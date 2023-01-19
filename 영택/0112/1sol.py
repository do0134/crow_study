left = list(input())
right = list()
t = int(input())


for _ in range(t) :
    fun = input()
    if " " in fun :
        fun, val = fun.split()
        if fun == "P":
            left.append(val)
    if fun == "L" :
        if left :
            right.append(left.pop())
    elif fun == "D" :
        if right :
            left.append(right.pop())
    elif fun == "B" :
        if left :
            left.pop()

right.reverse()
print("".join(left+right))


