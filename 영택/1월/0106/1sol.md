# leetcode 1833. Maximum Ice Cream Bars
# https://leetcode.com/problems/maximum-ice-cream-bars/description/

## 문제요약 
1. 아이스크림 가격이 List로 주어질 때, 주어진 돈으로 살 수 있는 아이스크림 수 최댓값

## 풀이요약
1. 아이스크림 가격을 정렬한다.
2. 반복문을 돌면서 주어진 돈에서 해당 인덱스 아이스크림 가격만큼 뺀다.
2-1. 주어진 돈이 다 떨어진다면 반복문을 멈춘다.
2-2. 인덱스가 리스트 길이보다 길어진다면 반복문을 멈춘다.