
# 실수를 했을 가능성이 있는가 X, 규칙을 지켜서 진행한 틱택토에서 나올 수 있는 상황인가 O
def solution(board):
    answer = -1
    # 선공 O, 후공 X, 빈칸 .
    # 1. 아무것도 없어도 됨
    if board == ["...", "...", "..."]:
        answer = 1
    else:
        ocnt = xcnt = 0
        completeO = completeX = 0
        for i in range(3):
            for j in range(3):
                # O와 X의 개수
                if board[i][j] == "O":
                    ocnt += 1
                elif board[i][j] == "X":
                    xcnt += 1
            # 가로
            if board[i] == "OOO":
                completeO += 1
            elif board[i] == "XXX":
                completeX += 1
        # 세로
        for j in range(3):
            if board[0][j] == board[1][j] == board[2][j]:
                if board[0][j] == "O":
                    completeO += 1
                elif board[0][j] == "X":
                    completeX += 1
        # 대각선
        if board[0][0] == board[1][1] == board[2][2]:
            if board[0][0] == "O":
                completeO += 1
            elif board[0][0] == "X":
                completeX += 1
        # 대각선
        if board[0][2] == board[1][1] == board[2][0]:
            if board[0][0] == "O":
                completeO += 1
            elif board[0][0] == "X":
                completeX += 1
        # 2. 항상 O의 개수 = X의 개수 아님 X의 개수 + 1
        if ocnt < xcnt or ocnt - xcnt > 1:
            answer = 0
        # 3. O가 연속3개인데 X가 3개면 안됨
        elif completeO == 1 and xcnt == ocnt:
            answer = 0
        # 4. X가 연속3개인데 O가 3개 초과면 안됨
        elif completeX == 1 and ocnt > xcnt:
            answer = 0
        # 5. O줄의 개수 + X줄의 개수 > 1이면 안됨
        # 근데 O줄이 2개고 X줄이 0개일 때 O의 개수 - X의 개수 = 1이면 됨
        elif completeO + completeX > 1:
            if completeO > 1 and ocnt - xcnt == 1:
                answer = 1
            else:
                answer = 0
        else:
            answer = 1

    return answer


b1 = ["O.X", ".O.", "..X"]
b2 = ["OOO", "...", "XXX"]
b3 = ["XOX", "OOO", "XOX"]
print(solution(b3))