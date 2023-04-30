// programmers 연습문제 - 대충 만든 자판
// https://school.programmers.co.kr/learn/courses/30/lessons/160586

package al_0430;

public class pro_0430_1 {
	class Solution {
	    public int[] solution(String[] keymap, String[] targets) {
	        int[] answer = new int[targets.length];
	        for (int i = 0; i < targets.length; i++) {
	            int cnt = 0;
	            for (int j = 0; j < targets[i].length(); j++) {
	                int k = 0;
	                boolean flag = false;
	                while (k < 100) {
	                    for (int l = 0; l < keymap.length; l++) {
	                        if (k >= keymap[l].length()) {
	                            continue;
	                        }
	                        if (targets[i].substring(j, j+1).equals(keymap[l].substring(k, k+1))) {
	                            cnt += (k+1);
	                            flag = true;
	                            break;
	                        }
	                    }
	                    if (flag) {
	                        break;
	                    }
	                    k += 1;
	                }
	                if (!flag) {
	                    cnt = -1;
	                    break;
	                }
	            }
	            answer[i] = cnt;
	        }
	        return answer;
	    }
	}

}
