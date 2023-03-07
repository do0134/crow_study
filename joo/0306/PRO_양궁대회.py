# programmers 2022 kakao blind recruitment - 양궁대회
# https://school.programmers.co.kr/learn/courses/30/lessons/92342


# 라이언은 무조건 어피치보다 많이 맞혀야 점수를 가져갈 수 있음
# 최종 점수가 같은 경우 어피치를 우승자로 결정
# 가장 큰 점수 차로 이기기 위해 어떤 과녁 점수에 맞혀야하는지 !
from itertools import product


def solution(n, info):
    answer = [-1]
    # 인덱스를 점수로 사용하기 위해 reverse 해주기
    info.reverse()
    # 차이의 최대값을 저장하는 변수
    dmax = 0
    # 라이언이 획득할 점수를 True, False를 11개로 조합을 사용하여 만들기
    for point in product((True, False), repeat=11):
        # True인 점수를 어피치가 쏜 화살 + 1개로 계산하여 총합 구하기
        point_sum = sum(info[i] + 1 for i in range(11) if point[i])
        # 화살 총합이 라이언이 쏠 수 있는 화살수 이하면 가능한 경우이기 때문에 점수 계산
        if point_sum <= n:
            # 어피치 : 본인이 화살을 쏜 점수 이고 라이언이 획득하지 못한 점수인 점수 더하기
            # 라이언 : 본인이 획득한 점수 더하기
            apeach = sum(i for i in range(11) if not point[i] and info[i])
            ryan = sum(i for i in range(11) if point[i])
            d = ryan - apeach
            # 라이언과 어피치의 점수 차가 현재 차이의 최댓값보다 크면
            # 최댓값 갱신, 라이언의 화살 리스트 갱신
            if d > dmax:
                dmax = d
                answer = [info[i] + 1 if point[i] else 0 for i in range(11)]
                # 라이언이 쏴야하는 총 화살 수에서 모자라는 화살 수 0점에 더해주기
                answer[0] += n - point_sum
    # 원래대로 리스트 되돌리기
    answer.reverse()
    return answer


n1 = 5
i1 = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
print(solution(n1, i1))
