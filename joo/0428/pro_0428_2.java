// programmers 2023 kakao blind recruitment - 개인정보 수집 유효 기간
// https://school.programmers.co.kr/learn/courses/30/lessons/150370

package al_0428;

import java.util.Map;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

public class pro_0428_2 {

	class Solution {
	    public List<Integer> solution(String today, String[] terms, String[] privacies) {
	        List<Integer> answer = new ArrayList<>();
	        String[] today_date = today.split("\\.");
	        Map<String, Integer> types = new HashMap<>();
	        for (int i = 0; i < terms.length; i++) {
	            String[] tmp = terms[i].split(" ");
	            types.put(tmp[0], Integer.parseInt(tmp[1]));
	        }
	        for (int i = 0; i < privacies.length; i++) {
	            int plus_year = 0;
	            String[] tmp = privacies[i].split(" ");
	            String[] date = tmp[0].split("\\.");
	            String type = tmp[1];
	            int end_month = Integer.parseInt(date[1]) + types.get(type);
	            while (end_month > 12) {
	                end_month -= 12;
	                plus_year += 1;
	            }
	            if (Integer.parseInt(date[0]) + plus_year < Integer.parseInt(today_date[0])) {
	                answer.add(i+1);
	            } else if (Integer.parseInt(date[0]) + plus_year > Integer.parseInt(today_date[0])) {
	               continue; 
	            } else {
	                if (end_month < Integer.parseInt(today_date[1]) || (end_month == Integer.parseInt(today_date[1]) && Integer.parseInt(today_date[2]) >= Integer.parseInt(date[2]))) {
	                    answer.add(i+1);
	                }
	            }
	        }
	        return answer;
	    }
	}

}
