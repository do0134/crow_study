# 프로그래머스 베스트앨범
# https://school.programmers.co.kr/learn/courses/30/lessons/42579

from collections import defaultdict

def solution(genres, plays):
    total = list()
    n = len(plays)
    cnt = defaultdict(list)

    for i in range(n):
        if genres[i] not in cnt:
            total.append([genres[i], plays[i]])
            cnt[genres[i]].append((i, plays[i]))

        else:
            for j in range(len(total)):
                if total[j][0] == genres[i]:
                    total[j][1] += plays[i]
                    break
            if len(cnt[genres[i]]) < 2:
                cnt[genres[i]].append((i, plays[i]))
            elif cnt[genres[i]][0][1] < plays[i]:
                cnt[genres[i]][0] = (i, plays[i])
            if cnt[genres[i]][1][1] < cnt[genres[i]][0][1]:
                cnt[genres[i]][0], cnt[genres[i]][1] = cnt[genres[i]][1], cnt[genres[i]][0]
            elif cnt[genres[i]][1][1] == cnt[genres[i]][0][1]:
                cnt[genres[i]].sort(reverse=True)

    total.sort(key=lambda x: x[1], reverse=True)
    answer = list()

    for g, p in total:
        for i in range(len(cnt[g]) - 1, -1, -1):
            answer.append(cnt[g][i][0])

    return answer