# leetcode 1071. Greatest Common Divisor of Strings
# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/

## 문제요약 
1. 두 개의 문자열에 대한 최대공약수를 구해라(str1 = str+str+str...이 되는 문자열)

## 풀이요약
1. 재귀로 모든 문자열을 확인하며 정답을 구했음.
2. 이 문제에 대해서 다르게 접근할 수 있는데, 최대공약수를 사용하는 것.  
    2-1 str1 + str2 와 str2 + str1이 같지 않다면 공약수가 없는 것이다.(최대 공약수가 성립히지 않는다는 말이다.)  
2-2 2-1의 예외처리만 한다음 str1[:math.gcd(len(str1),len(str2))]를 해준다면 문제를 해결할 수 있다.     
   2-3 최대공약수를 빗댄 건줄 알았지만, 정말 최대공약수를 구하면 쉽게 풀리는 문제 