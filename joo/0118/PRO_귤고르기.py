# programmers 연습문제 - 귤 고르기
# https://school.programmers.co.kr/learn/courses/30/lessons/138476


## 처음한 코드에서는 시간초과나는 케이스가 5개정도 있었다
## cnt를 있는 크기만 하지말고 그냥 처음부터 만들어놓고 하니까 해결 !

def solution(k, tangerine):
    answer = 0
    cnt = [[x, 0] for x in range(10000000)]
    for t in tangerine:
        cnt[t][1] += 1
    cnt.sort(key=lambda x: -x[1])

    total = 0
    for i in range(len(cnt)):
        total += cnt[i][1]
        answer += 1
        if total >= k:
            break

    return answer


k1 = 6
t1 = [1, 3, 2, 5, 4, 5, 2, 3]

k2 = 4
t2 = [1, 3, 2, 5, 4, 5, 2, 3]
print(solution(k2, t2))