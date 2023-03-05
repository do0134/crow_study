# leetcode 2444. Count Subarrays With Fixed Bounds
# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/description/

## 문제요약
1. 다음에 해당하는 부분수열의 수 찾아내기

    1. 부분수열의 최솟값이 minK, 최댓값이 maxK
    2. 부분수열은 연속된 인자들로 이루어져야 함.
    
## 풀이요약 
1. max_idx, min_idx를 찾은 다음, 해당 범위에서 벗어난 인덱스를 찾는다. 
2. 그리고 max_idx, min_idx 중 작은 값에 범위에서 벗어난 인덱스를 뺀다. 

## 원래 어떻게 하려고 했었냐면....
1. 왼쪽을 min_idx로 오른쪽을 max_idx로 찾아가며 하려고 했으나...
2. 왼쪽이 꼭 최솟값이 아닐 수도 있다는 예제가 있어서 풀이방법을 바꿔야 했다.
그러니까, 왼쪽이 최댓값이 되어도 된다. 그래서 풀이방법에서 min_idx, max_idx 중 작은 값에서 빼는 것