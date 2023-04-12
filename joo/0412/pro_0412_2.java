// https://school.programmers.co.kr/learn/courses/30/lessons/142086

package algorithm;

import java.util.Arrays;

public class pro_0412_2 {
//	private static int[] append(int[] arr, int ele) {
//		int[] array = new int[arr.length + 1];
//		System.arraycopy(arr, 0, array, 0, arr.length);
//		array[arr.length] = ele;
//		return array;
//	}
	
    public static int[] solution(String s) {
        int[] answer = new int[s.length()];
//        answer = append(answer, -1);
        answer[0] = -1;
        for (int i = 1; i < s.length(); i++) {
        	int cnt = 0;
        	for (int j = i-1; j >= 0; j--) {
        		if (s.charAt(i) == s.charAt(j)) {
        			cnt = i - j;
        			break;
        		}
        	}
        	System.out.println(cnt);
        	if (cnt != 0) {
//        		answer = append(answer, cnt);
        		answer[i] = cnt;
        	} else {
//        		answer = append(answer, -1);
        		answer[i] = -1;
        	}
        }
        System.out.println(Arrays.toString(answer));
        return answer;
    }
    public static void main(String[] args) {
    	System.out.println(solution("banana"));
    }

}
