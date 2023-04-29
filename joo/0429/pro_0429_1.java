// programmers 연습문제 - 기사단원의 무기
// https://school.programmers.co.kr/learn/courses/30/lessons/136798

package al_0429;

public class pro_0429_1 {
	class Solution {
	    public int solution(int number, int limit, int power) {
	        int answer = 0;
	        int[] cnt = new int[number+1];
	        
	        for (int i = 1; i <= number; i++) {
	            int now = i;
	            int x = 1;
	            while (now <= number) {
	                cnt[now] += 1;
	                x += 1;
	                now = i * x;
	            }
	        }
	        for (int i = 1; i <= number; i++) {
	            if (cnt[i] > limit) {
	                answer += power;
	            } else {
	                answer += cnt[i];
	            }
	        }
	        return answer;
	    }
	}

}
