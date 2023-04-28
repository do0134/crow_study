// programmers 연습문제 - 둘만의 암호
// https://school.programmers.co.kr/learn/courses/30/lessons/155652

package al_0428;

public class pro_0428_1 {

	class Solution {
	    public String solution(String s, String skip, int index) {
	        String answer = "";
	        for (int i = 0; i < s.length(); i++) {
	            int change = 0;
	            int now = (int)s.charAt(i);
	            while (change < index) {
	                now += 1;
	                if (now > 122) {
	                    now -= 26;
	                }
	                boolean flag = true;
	                for (int j = 0; j < skip.length(); j++) {
	                    if ((int)skip.charAt(j) == now) {
	                        flag = false;
	                        break;
	                    }
	                }
	                if (flag) {
	                    change += 1;
	                }
	            }
	            answer += String.valueOf((char)now);
	        }
	        return answer;
	    }
	}
}
