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
	            flag = false;
	            if (s.substring(i, i+1).equals(now)) {
	                now_cnt += 1;
	                System.out.println("now equal");
	                System.out.println(now_cnt);
	            } else {
	                not_now_cnt += 1;
	                System.out.println("not equal");
	                System.out.println(not_now_cnt);
	            }
	            if (now_cnt == not_now_cnt) {
	                answer += 1;
	                now_cnt = 1;
	                not_now_cnt = 0;
	                flag = true;
	                System.out.println("cnt equal");
	                System.out.println(answer);
	                
	            }
	            if (i != s.length()-1) {
	                now = s.substring(i+1, i+2);
	                System.out.println("now change");
	                System.out.println(now);
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
