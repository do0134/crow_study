// programmers 2021 카카오 채용연계형 인턴십 - 숫자 문자열과 영단어
// https://school.programmers.co.kr/learn/courses/30/lessons/81301?language=java

package al_0413;

public class pro_0413_1 {
	
	class Solution {
	    public static int solution(String s) {
	        int answer = 0;
	        String str_ans = "";
	        String[] nums = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
	        int index = 0;
	        while (index < s.length()) {
	        	if (Character.isDigit(s.charAt(index))) {
	        		str_ans += s.charAt(index);
	        		index ++;
	        	}
	        	else {
	        		for (int i = 0; i < 10; i++) {
		        		if (index + nums[i].length() <= s.length() && nums[i].equals(s.substring(index, index + nums[i].length()))) {
		        			str_ans += Integer.toString(i);
		        			index += nums[i].length();
		        			break;
		        		}
		        	}
	        	}
	        }
	        answer = Integer.parseInt(str_ans);
	        return answer;
	    }
	}
	
	public static void main(String[] args) {
		System.out.println(Solution.solution("123"));
	}

}
