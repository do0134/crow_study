# leetcode 787. Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

## 문제요약
1. 가중치가 있는 단방향 그래프에서 시작점과 도착점을 제한된 움직임 안에서 갈 수 있는 가장 적은 가중치를 구하기

## 풀이요약
1. 다익스트라로 풀려고 했지만, BFS+DP로 품
2. 2중 배열로 airport[from][to] = cost 형식의 그래프를 만듦
3. bfs를 돌며 현재 코스트 + 다음 코스트가 dp[next_place]보다 적다면 갱신하고 다시 BFS를 도는 형식
4. clean code 책을 보며 명명법에 조금 신경쓰려고 했음. 그런데 for 루프를 돌 때 k 변수가 겹쳐, 영문도 모른채 틀렸다....