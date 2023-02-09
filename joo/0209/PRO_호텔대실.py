# PROGRAMMERS 연습문제 - 호텔 대실
# https://school.programmers.co.kr/learn/courses/30/lessons/155651

# 시간을 분으로 바꿔서 사용
def time_change(string):
    h, m = map(int, string.split(":"))
    return h * 60 + m


def solution(book_time):
    answer = 0
    check = list()
    # 1 : 입실, 0: 퇴실
    # 입실과 퇴실 시간을 구분하되 한 리스트에 넣고 오름차순으로 정렬
    for start, end in book_time:
        check.append((time_change(start), 1))
        check.append((time_change(end) + 10, 0))
    check.sort()

    # 시간순으로 확인하며 입실이면 +1 퇴실이면 -1을 해주며 최대값 갱신
    tmp = 0
    for time, ch in check:
        tmp += -1 if ch == 0 else 1
        answer = max(answer, tmp)
    return answer


b1 = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]

print(solution(b1))
