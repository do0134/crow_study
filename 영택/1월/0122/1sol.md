# leetcode 131. Palindrome Partitioning
# https://leetcode.com/problems/palindrome-partitioning/description/

## 문제요약
1. 문자열이 주어질 때, 해당 문자열로 만들어낼 수 있는 조합 중 모든 부분집합이 회문인 조합을 찾아라

## 풀이요약
1. 백트래킹 사용
2. len(s)//2+1만큼 for문을 돌아서 s[i]와 s[-(i+1)]이 같은지 확인
3. 회문이라면 재귀로 백트래킹을 돌고, 아니면 넘긴다. 처음 들어간 문자열을 모두 사용했다면, answer에 append한다.