// programmers 성격 유형 검사하기
// https://school.programmers.co.kr/learn/courses/30/lessons/118666

package al_0427;

import java.util.Map;
import java.util.HashMap;

public class pro_0427_2 {

	class Solution {
	    public String solution(String[] survey, int[] choices) {
	        String answer = "";
	        Map<String, Integer> score = new HashMap<>();
	        score.put("A", 0);
	        score.put("N", 0);
	        score.put("J", 0);
	        score.put("M", 0);
	        score.put("C", 0);
	        score.put("F", 0);
	        score.put("R", 0);
	        score.put("T", 0);
	        for (int i = 0; i < survey.length; i++) {
	            if (choices[i] > 4) {
	                score.put(survey[i].substring(1, 2), score.get(survey[i].substring(1, 2)) + choices[i] - 4);
	            } else {
	                score.put(survey[i].substring(0, 1), score.get(survey[i].substring(0, 1)) + 4 - choices[i]);
	            }
	        }
	        if (score.get("R") >= score.get("T")) {
	            answer += "R";
	        } else {
	            answer += "T";
	        }
	        if (score.get("C") >= score.get("F")) {
	            answer += "C";
	        } else {
	            answer += "F";
	        }
	        if (score.get("J") >= score.get("M")) {
	            answer += "J";
	        } else {
	            answer += "M";
	        }
	        if (score.get("A") >= score.get("N")) {
	            answer += "A";
	        } else {
	            answer += "N";
	        }
	        
	        return answer;
	    }
	}
}
