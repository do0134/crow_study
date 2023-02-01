# leetcode 1443. Minimum Time to Collect All Apples in a Tree
# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/description/

## 문제요약
1. root에서 시작해서 tree에 있는 apple을 모두 따올 수 있는 이동거리

## 풀이요약
1. tree배열을 만들어 간선에 대한 정보를 저장한다.
2. dfs를 돌아 apple이거나 더 나아간 거리를 계속 더한다. 