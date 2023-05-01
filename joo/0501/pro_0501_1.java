// programmers 연습문제 - 문자열 나누기
// https://school.programmers.co.kr/learn/courses/30/lessons/140108


package al_0501;

public class pro_0501_1 {
	class Solution {
	    public int solution(String s) {
	        int answer = 0;
	        String now = s.substring(0, 1);
	        int now_cnt = 1;
	        int not_now_cnt = 0;
	        int i = 1;
	        boolean flag = false;
	        while (i < s.length()) {
	            if (s.substring(i, i+1).equals(now)) {
	                now_cnt += 1;
	            } else {
	                not_now_cnt += 1;
	            }
	            if (now_cnt == not_now_cnt) {
	                answer += 1;
	                now_cnt = 1;
	                not_now_cnt = 0;
	                flag = true;
	                
	            }
	            if (flag && i != s.length()-1) {
	                flag = false;
	                now = s.substring(i+1, i+2);
	                i += 1;
	            }
	            i += 1;
	        }
	        if (!flag) {
	            answer += 1;
	        }
	        return answer;
	    }
	}
}
