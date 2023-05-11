// 프로그래머스 2023 kakao blind recruitment - 택배 배달과 수거하기
// https://school.programmers.co.kr/learn/courses/30/lessons/150369?language=java

package al_0511;

public class pro_0511_1 {
	class Solution {
	    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
	        long answer = 0;
	        int deli = 0;
	        int pick = 0;
	        for (int i = n-1; i >= 0; i--) {
	            deli += deliveries[i];
	            pick += pickups[i];
	            
	            while (deli > 0 || pick > 0) {
	                deli -= cap;
	                pick -= cap;
	                answer += ((i+1) * 2);
	            }
	        }
	        return answer;
	    }
	}

}
