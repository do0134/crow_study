# 백준 1918 후위 표기식
# https://www.acmicpc.net/problem/1918

s = input()
# 연산자 우선순위
priority = {"+" : 2, "-" : 2, "*" : 1, "/" : 1 ,"(" : 0, ")" : 0}
# 정답을 순서대로 담을 배열
answer = list()
# 연산자를 담을 임시 배열
stack = list()



for i in s :
    # 문자라면 바로 append
    if i not in priority :
        answer.append(i)

    # 괄호라도 바로 append
    elif i == "(" :
        stack.append(i)

    # 닫히는 괄호라면 (를 만날 때까지 pop
    elif i == ")" :
        temp = stack.pop()
        while temp != "(" :
            answer.append(temp)
            temp = stack.pop()

    # 연산자라면
    elif i in priority :
        # stack이 비워져있다면 일단 담는다.
        if not stack :
            stack.append(i)
        # stack 마지막 연산자보다 i의 우선순위가 높다면(늦게 연산해야한다면)
        # <= 인 이유는 먼저 온 연산자를 먼저 연산하기 때문
        elif priority[stack[-1]] <= priority[i]:
            # 괄호는 pop하면 안 되기 때문에 예외처리
            while stack and (priority[stack[-1]] <= priority[i] and stack[-1] != "(") :
                answer.append(stack.pop())
            stack.append(i)
        else:
            stack.append(i)

while stack :
    answer.append(stack.pop())
print("".join(answer))





