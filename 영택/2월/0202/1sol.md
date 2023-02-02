# leetcode 953. Verifying an Alien Dictionary
# https://leetcode.com/problems/verifying-an-alien-dictionary/description/

## 문제요약
1. 주어진 문자열 리스트를 보고, 그 문자열 리스트의 사전적 방식에 맞게 a-z가 정렬되었는지 확인

## 풀이요약
1. 주어진 a-z를 char : idx 방식으로 저장한다. 
2. zip으로 반복문 2개를 돌면서 서로 확인한다.

## 오래 걸린 이유
독해력이 부족했는지 모르겠지만, 3번째 예제의 예시가 어려웠다. 분명 사전적인 순서를 임의로 바꾸고 그대로 문자열이 나열되어있는지 확인하는 문제다.
그러나 기본 사전적인 방식은 따른다. 
예를 들어 [apple, app] 은 뒤에 걸 볼 거 없이 False다. 왜냐하면 사전적인 방식으로 빈 칸은 어떤 문자보다 우선해야 하기 때문....
이걸 몰라서 Easy 난이도였지만 한참걸림