# leetcode 1519. Number of Nodes in the Sub-Tree With the Same Label
# https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/description/

## 문제요약
- 노드들에 a,b,c,d....라벨을 붙임
- 자손 노드들 중 같은 라벨을 가지고 있는 자손 수를 찾는 문제

## 풀이요약
- DFS로 완전 탐색
- Counter 배열을 활용하여 해당 노드 자손이 몇 개인지 재귀적으로 찾아내면서 정답을 채울 것
