// 프로그래머스 연습문제 - 롤케이크 자르기
// https://school.programmers.co.kr/learn/courses/30/lessons/132265

package al_0510;

import java.util.*;

public class pro_0510_1 {

	class Solution {
	    public int solution(int[] topping) {
	        int answer = 0;
	        Set<Integer> first = new HashSet<>();
	        Map<Integer, Integer> second = new HashMap<>();
	        for (int i = 1; i < topping.length; i++) {
	            second.put(topping[i], second.getOrDefault(topping[i], 0) + 1);
	        }
	        first.add(topping[0]);
	        for (int i = 1; i < topping.length; i++) {
	            first.add(topping[i]);
	            second.put(topping[i], second.get(topping[i]) - 1);
	            if (second.get(topping[i]) == 0) {
	                second.remove(topping[i]);
	            }
	            if (first.size() == second.size()) {
	                answer += 1;
	            }
	        }
	        return answer;
	    }
	}

}
