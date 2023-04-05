# BOJ 14725 개미굴
# https://www.acmicpc.net/problem/14725
# 5
# 2 KIWI BANANA
# 2 KIWI APPLE
# 4 APPLE BANANA KIWI STRAW
# 4 APPLE BANANA KIWI ORANGE
# 3 APPLE BANANA ORANGE

# 틀렸습니다 나오는데 뭐가 틀린지 모르겠음
# 예제도 다 맞고 테케 찾아본거랑 생각해낸거 다 해봤는데 맞음,,
# 찾아보니까 Trie..? 구조를 써야한다구,,? 먼지 모름
N = int(input())
arr = []
for _ in range(N):
    lst = list(input().split())
    arr.append(lst[1:])
arr.sort()
start = ''
ans = ''
now = []
for i in range(N):
    if start != arr[i][0]:
        now = [[] for _ in range(16)]
        start = arr[i][0]
        ans += arr[i][0] + '\n'
    for j in range(1, len(arr[i])):
        if arr[i][j] not in now[j]:
            ans += ('--' * j) + arr[i][j] + '\n'
            now[j].append(arr[i][j])

print(ans.rstrip())

