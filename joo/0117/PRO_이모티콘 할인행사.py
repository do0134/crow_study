# programmers 2023 kakao blind recruitment - 이모티콘 할인행사
# https://school.programmers.co.kr/learn/courses/30/lessons/150368

import itertools

def solution(users, emoticons):
    answer = [0, 0]
    sales = [40, 30, 20, 10]
    # 각 이모티콘 별로 할인율 나올 수 있는 조합
    discount = list(itertools.product(sales, repeat=len(emoticons)))
    for d in discount:
        # 할인 후 user별 구매 총액
        dis_user = [0 for _ in range(len(users))]
        # [플러스 가입자 수, 구매 총액]
        buyed = [0, 0]
        for i in range(len(emoticons)):
            # 각 user별로 금액 더해주기
            for k in range(len(users)):
                if users[k][0] <= d[i]:
                    dis_user[k] += emoticons[i] * (100 - d[i]) / 100
        # 플러스 가입 유무
        for j in range(len(users)):
            if dis_user[j] >= users[j][1]:
                buyed[0] += 1
            else:
                buyed[1] += int(dis_user[j])
        if answer[0] < buyed[0]:
            answer = buyed
        elif answer[0] == buyed[0]:
            answer[1] = max(buyed[1], answer[1])
    return answer


u = [[40, 10000], [25, 10000]]
e = [7000, 9000]
u2 = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
e2 = [1300, 1500, 1600, 4900]
print(solution(u2, e2))