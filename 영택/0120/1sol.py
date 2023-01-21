n = int(input())
i = 1
arr = list()
arr2 = list()

while i <= n :
    if n%i == 0 :
        if i %2 == 0 :
            arr.append(i)
        else :
            arr2.append(i)
    i += 1

print(arr)
print(arr2)