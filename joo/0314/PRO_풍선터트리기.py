# programmers 월간 코드 챌린지 시즌1 - 풍선 터트리기
# https://school.programmers.co.kr/learn/courses/30/lessons/68646

# 내가 생각한 방식대로 풀었더니 답이 원하는 대로 나오지 않아 답답해하다가
# 접근법 힌트를 보고 ,,, 싹 갈아엎었다
# 어떻게 저런 생각을 할까..? 부러웠다

# 힌트를 얻은 접근법과 결론

# 문제에 최대 한 번 더 작은 번호를 터트릴 수 있다는 조건이 있는데
# 이 조건이 없었다면 어떤 경우에도 마지막에는 가장 작은 번호만 남는다
# 즉, 가장 작은 번호가 아닌 풍선이 남기 위해서는 작은 번호를 터트릴 수 있는 기회를 이용해
# 가장 작은 번호의 풍선을 터트리는 것을 반드시 해줘야 한다
# 그리고 가장 작은 번호(min)의 풍선은 어떤 풍선이든 제거할 수 있다
# 따라서 min 풍선의 왼쪽에 있는 풍선들은 해당 풍선의 오른쪽은 min 풍선이 다 없애주기 때문에
# 본인의 왼쪽에 있는 풍선만 다 제거할 수 있으면 된다
# min의 오른쪽에 있는 풍선은 본인의 오른쪽에 있는 풍선을 제거할 수 있어야 한다
# 즉, 양 끝에서 출발해 min 풍선까지 최솟값을 갱신해가며 최솟값 이하가 나오는 경우의 개수를 세면 된다

def solution(a):
    answer = 0
    minn = min(a)
    r_now_min = l_now_min = 10 ** 9
    rcnt = lcnt = 0
    for num in a:
        if num == minn:
            break
        if num < l_now_min:
            l_now_min = num
            lcnt += 1
    for i in range(len(a) - 1, -1, -1):
        if a[i] == minn:
            break
        if a[i] < r_now_min:
            r_now_min = a[i]
            rcnt += 1
    answer = lcnt + rcnt + 1
    return answer


a1 = [9, -1, -5]
a2 = [-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]
print(solution(a1))
