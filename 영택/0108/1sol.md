# 149. Max Points on a Line
# https://leetcode.com/problems/max-points-on-a-line/description/

## 문제요약
1. 2차원 평면 좌표값이 List로 주어질 때, 선 하나를 그어서 지날 수 있는 좌표의 최댓값 구하기

## 풀이요약
1. 2중 반복문을 돌 예정
1-1. 첫 번째 반복문에서 2개의 변수 생성
1-2. 좌표값이 같을 수 있기 때문에 same이라는 변수 생성
1-3. 기울기가 같으면 한 선에 있을 수 있음. 기울기를 key값으로, 지나는 좌표를 value값으로 가지는 dictionary 생성

2. 2번째 반복문에서 1번 반복문의 좌표와 x, y값 차이를 구해서 기울기 구함.
2-1. dx, dy(x,y의 차이)를 구해서 dy/dx를 구한다. 
2-2. dx, dy가 0일 때 동일한 좌표이기 때문에, same에 더해주고 다음으로 넘긴다.
2-3. 좌표가 같지 않다면 dx가 0일 때만 예외처리 해준다. dx가 0일 때는 미리 정해둔 고유 key값에 +1을 해준다.(zerodivision error를 피하기 위함)
2-4. 아니라면 dy/dx의 value값에 +1을 해준다.
2-5. 2번째 반복문이 끝나면 same + max(dictionary.values()) 값이 기존 최댓값보다 큰지 비교한다. 