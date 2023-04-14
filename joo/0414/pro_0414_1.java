// programmers 연습문제 - 과일장수
// https://school.programmers.co.kr/learn/courses/30/lessons/135808


package al_0414;

import java.util.Arrays;

public class pro_0414_1 {
	class Solution {
		private static void reversesort(int[] arr) {
			Arrays.sort(arr);
			for (int i = 0;i < (arr.length / 2); i ++) {
				int tmp = arr[i];
				arr[i] = arr[arr.length - i - 1];
				arr[arr.length - i - 1] = tmp;
			}
		}
		
	    public static int solution(int k, int m, int[] score) {
	        int answer = 0;
	        reversesort(score);
//	        System.out.println(Arrays.toString(score));
	        for (int i = 0; i < score.length; i+=m) {
	        	if (i + m <= score.length) {
	        		answer += (score[i+m-1] * m);
	        	}
	        }
	        return answer;
	    }
	}
	public static void main(String[] args) {
		int k1 = 3; int m1 = 4; int[] s1 = {1, 2, 3, 1, 2, 3, 1};
		int k2 = 4; int m2 = 3; int[] s2 = {4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2};
		System.out.println(Solution.solution(k1, m1, s1));
		System.out.println(Solution.solution(k2, m2, s2));
	}

}
