# programmers 연습문제 - 두 원 사이의 정수 쌍
# https://school.programmers.co.kr/learn/courses/30/lessons/181187


def solution(r1, r2):
    answer = 0
    zero = 0
    for x in range(r2+1):
        bt = (r2**2 - x**2)**(1/2)
        if x > r1:
            st = 0
        else:
            st = (r1**2 - x**2)**(1/2)
        # 원 사이에 있는 (작은 원 선 위의 점 제외) 점 개수
        now = int(bt.real) - int(st.real)
        # 작은 원 선 위의 점 더해주기
        if int(st.real) == st.real:
            now += 1
        # y축 위의 점의 개수
        if x == 0:
            zero += now
        # x축 위의 점의 개수
        if st == 0:
            zero += 1
        answer += now
    # 4사분면 곱해준 뒤 축 위의 점 개수 빼주기
    answer = (answer * 4) - (zero * 2)
    return answer