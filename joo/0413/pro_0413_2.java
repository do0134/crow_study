// programmers 연습문제 - 삼총사
// https://school.programmers.co.kr/learn/courses/30/lessons/131705

package al_0413;

import java.util.ArrayList;

public class pro_0413_2 {
	class Solution {
		static ArrayList<int[]> combs = new ArrayList<>();
		static void combination(int[] arr, boolean[] visited, int start, int n, int r) {
			if (r == 0) {
				int[] comb = new int[3];
				int idx = 0;
				for (int i = 0; i < arr.length; i++) {
					if (visited[i]) {
						comb[idx] = arr[i];
						idx ++;
					}
				}
				combs.add(comb);
				return;
			}
			for (int i = start; i < n; i++) {
				visited[i] = true;
				combination(arr, visited, i+1, n, r-1);
				visited[i] = false;
			}
		}
		
	    public static int solution(int[] number) {
	        int answer = 0;
	        int[] arr = new int[number.length];
	        boolean[] visited = new boolean[number.length];
	        for (int i = 0; i < number.length; i++) {
	        	arr[i] = i;
	        }

	        combination(arr, visited, 0, number.length, 3);

	        for (int i = 0; i < combs.size(); i++) {
	        	int total = 0;
	        	for (int j = 0; j < 3; j++) {
	        		total += number[combs.get(i)[j]];
	        	}
	        	if (total == 0) {
	        		answer++;
	        	}
	        }
	        return answer;
	    }
	}
	
	public static void main(String[] args) {
		int[] nums1 = {-2, 3, 0, 2, -5};
		int[] nums2 = {-3, -2, -1, 0, 1, 2, 3};
		int[] nums3 = {-1, 1, -1, 1};
		System.out.println(Solution.solution(nums3));
	}

}
