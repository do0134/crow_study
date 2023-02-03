# https://www.acmicpc.net/problem/25757
N, game = input().split()
N = int(N)
arr = [input() for _ in range(N)]
answer = list(set(arr))

# 임스와 플레이 해야하기 때문에 플레이 인원에서 -1명 해야 함
if game == "Y":
    print(len(answer))
elif game == "F":
    print(len(answer) // 2)
elif game == "O":
    print(len(answer) // 3)