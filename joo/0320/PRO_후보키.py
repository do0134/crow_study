# programmers 2019 kakao blind recruitment - 후보키
# https://school.programmers.co.kr/learn/courses/30/lessons/42890


from itertools import combinations


def solution(relation):
    answer = 0
    combs = []
    for n in range(1, len(relation)):
        tmp = combinations(list(range(len(relation[0]))), n)
        combs += tmp

    # 유일성을 만족하는 키 구하기
    can_key = []
    for i in range(len(combs)):
        dic = dict()
        for j in range(len(relation)):
            key = ''
            for idx in combs[i]:
                key += str(relation[j][idx])
            if key in dic.keys():
                break
            else:
                dic[key] = 1
        else:
            can_key.append(combs[i])
    # print(can_key)

    # 최소성을 만족하는 키만 구하기
    now = 0
    while now < len(can_key) - 1:
        search = now + 1
        while search < len(can_key):
            # search 튜플에 now 튜플이 모두 속해있는지 확인
            if len(set(can_key[now] + can_key[search])) == len(can_key[search]):
                can_key.pop(search)
            else:
                search += 1
        now += 1
    # print(can_key)
    answer = len(can_key)
    return answer


r1 = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
      ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]
r2 = [['a', 1, 'aaa', 'c', 'ng'], ['b', 1, 'bbb', 'c', 'g'], ['c', 1, 'aaa', 'd', 'ng'], ['d', 2, 'bbb', 'd', 'ng']]
print(solution(r2))
