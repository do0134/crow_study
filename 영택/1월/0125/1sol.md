# leetcode 2359. Find Closest Node to Given Two Nodes
# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/description/

## 문제요약
1. node1, node2와 edges 배열이 주어질 때 두 점에서 도착할 수 있으면서, 가장 먼 거리를 가는 점 구하기

## 풀이요약
1. dfs로 node1, node2에서 도착할 수 있는 지점을 몇 번 움직임으로 갈 수 있는지 파악
2. n번(edges의 수)반복문을 돌며 도착할 수 있는 지점의 거리를 비교하여 기존 answer보다 크다면 answer 갱신