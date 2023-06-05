n, s = map(int,input().split())
arr = list(map(int,input().split()))
answer = 0
for i in range(n) :
    for j in range(n-i):
        print(arr[j:j+i+1])
        if sum(arr[j:j+i+1]) == s :
            answer += 1

print(answer)