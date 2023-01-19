# leetcode 452. Minimum Number of Arrows to Burst Balloons
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/

## 문제설명 
1. 번호가 달린 풍선의 연결된 범위가 주어질 때 풍선을 모두 터뜨릴 수 있는 최소한의 풍선 수
2. 단 한 풍선은 여러 연결점을 가질 수 있으며, 풍선이 터질 때 연결된 풍선 모두 터짐

## 풀이설명
1. [start, end] 형식으로 되어있기 때문에 end를 기준으로 정렬
1-1 .sort()와 sorted()사이에 꽤 유의미한 시간차이가 존재함. why? 몰?루? 왜 sorted가 빠르지...
2. end를 기준으로 정렬했기 때문에 end보다 start가 커지는 순간 풍선을 하나씩 더 터뜨리는게 가장 최소한으로 터뜨리는 방법
3. for 문을 돌아서 2에 해당하는 구간을 찾아 answer에 1씩 더한다.
3-1. 터뜨릴 풍선 변수 answer 초기값은 1로 둔다.
3-2. points[i][1]을 max_value값 초기값으로 두고 i[0]가 max_value 커질 때마다 answer와 max_value 갱신