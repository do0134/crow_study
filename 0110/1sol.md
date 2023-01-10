# leetcode 100. Same Tree
# https://leetcode.com/problems/same-tree/description/

## 문제요약
1. 주어진 두 개의 B-트리가 동일한 지 확인하는 문제

## 풀이요약
1. BFS로 완전탐색해서 모든 노드에 동일한 value값이 들어있는지 확인
2. if 문을 사용해서 and에 걸리면 동일하기 때문에 계속 진행, or에 걸리면 다르기 때문에 False 리턴