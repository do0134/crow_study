# https://www.acmicpc.net/problem/13305
N = int(input())
roadLen = list(map(int, input().split()))
city = list(map(int, input().split()))
answer = 0

# 요 패턴은 외워버리는 게 좋겠다,,,왜 이걸 생각 못하니?
# 기준값
current = city[0]
for i in range(N - 1):
    # 비교값이 더 작으면
    if current > city[i]:
        # 기준값 갱신!
        current = city[i]
    # 기준값에 현 가중치만큼 주유해준다
    answer += current * roadLen[i]
print(answer)