# softeer [인증평가(5차) 기출] 성적 평가 - 등수구하기
# https://softeer.ai/practice/info.do?idx=1&eid=1309&sw_prbl_sbms_sn=130673

import sys
import copy
from collections import defaultdict, Counter

n = int(sys.stdin.readline())
dp = [0] * n


def make_dict(r_list):
    r_dict = defaultdict(int)
    r_cnt = Counter(r_list)
    rank = 1
    r_list = list(set(r_list))
    for i in range(len(r_list)):
        if i == 0:
            r_dict[r_list[i]] = rank
        else:
            rank = rank + r_cnt[r_list[i - 1]]
            r_dict[r_list[i]] = rank

    return r_dict


for _ in range(3):
    temp = list(map(int, sys.stdin.readline().split()))
    temp1 = copy.deepcopy(temp)
    temp1.sort(reverse=True)
    rank_dict = make_dict(temp1)
    answer_list = list()
    for i in range(n):
        dp[i] += temp[i]

        answer_list.append(rank_dict[temp[i]])
    print(*answer_list)

answer = list()
answer_dict = make_dict(sorted(dp, reverse=True))
for i in range(n):
    answer.append(answer_dict[dp[i]])
print(*answer)