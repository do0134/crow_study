# https://www.acmicpc.net/problem/4659
# 문자열, 구현
while True:
    password = input()
    if password == 'end':
        break
    vowels = 'aeiou'

    vowels_cnt = 0
    vowels_repeat = consonant_repeat = 0
    temp = ""
    flag = True
    for i in password:
        # 모음일 때
        if i in vowels:
            # 자음 반복 초기화
            consonant_repeat = 0
            vowels_cnt += 1
            vowels_repeat += 1
            if 3 <= vowels_repeat:
                flag = False
            # ee or oo 체크 (2글자 연속 중 예외)
            elif temp == i:
                if i == 'e' or i == 'o':
                    pass
                else:
                    flag = False
        # 자음일 때
        else:
            # 모음 반복 초기화
            vowels_repeat = 0
            consonant_repeat += 1
            if 3 <= consonant_repeat:
                flag = False
            elif temp == i:
                flag = False
        temp = i
    if vowels_cnt < 1:
        flag = False
    if flag:
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')