// programmers 로또의 최고 순위와 최저 순위
// https://school.programmers.co.kr/learn/courses/30/lessons/77484?language=java

package al_0427;

import java.util.Map;
import java.util.HashMap;

public class pro_0427_1 {

	class Solution {
	    public int[] solution(int[] lottos, int[] win_nums) {
	        Map<Integer, Integer> grade = new HashMap<>();
	        grade.put(6, 1); grade.put(5, 2); grade.put(4, 3);
	        grade.put(3, 4); grade.put(2, 5); grade.put(1, 6); grade.put(0, 6);
	        int[] answer = new int[2];
	        int minn = 0;
	        int maxx = 0;
	        for (int num : win_nums) {
	            for (int el : lottos) {
	                if (num == el) {
	                    minn += 1;
	                    break;
	                }
	            }
	        }
	        for (int el : lottos) {
	            if (el == 0) {
	                maxx += 1;
	            }
	        }
	        maxx += minn;
	        answer[0] = grade.get(maxx);
	        answer[1] = grade.get(minn);
	        
	        return answer;
	    }
	}

}
