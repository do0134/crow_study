// programmers 연습문제 - 햄버거 만들기
// https://school.programmers.co.kr/learn/courses/30/lessons/133502

package al_0414;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class pro_0414_2 {
	class Solution {
	    public static int solution(int[] ingredient) {
	        int answer = 0;
	        int idx = 0;
//	        int[] nextIdx = new int[ingredient.length];
//	        for (int i = 0; i < ingredient.length; i++) {
//	        	nextIdx[i] = i+1;
//	        }
//	        while(idx < ingredient.length-3) {
//	        	if (nextIdx[idx] == 0) {
//	        		idx++;
//	        		continue;
//	        	}
//	        	if (ingredient[idx] == 1 
//	        			&& nextIdx[idx] < ingredient.length && ingredient[nextIdx[idx]] == 2 
//	        			&& nextIdx[nextIdx[idx]] < ingredient.length && ingredient[nextIdx[nextIdx[idx]]] == 3 
//	        			&& nextIdx[nextIdx[nextIdx[idx]]] < ingredient.length && ingredient[nextIdx[nextIdx[nextIdx[idx]]]] == 1) {
//	        		nextIdx[idx] = nextIdx[nextIdx[idx]] = nextIdx[nextIdx[nextIdx[idx]]] = nextIdx[nextIdx[nextIdx[nextIdx[idx]]]] = 0;
//	        		answer ++;
//	        		if (idx != 0) {
//	        			nextIdx[idx-1] = idx + 4;
//	        			idx = 0;
//	        			continue;
//	        		}
//	        	}
//	        	idx ++;
//	        }
	        List<Integer> ingredientList = new ArrayList<>();
	        for (int el : ingredient) {
	        	ingredientList.add(el);
	        }
//	        System.out.println(ingredientList);
	        Stack<Integer> stack = new Stack<>();
	        int floor = 0;
	        boolean flag = false;
	        
	        while (ingredientList.size() != 0 && floor < ingredientList.size()) {
	        	switch (ingredientList.get(floor)) {
		        	case 1:
		        		if (stack.size() != 0 && stack.peek() == 3) {
		        			answer ++;
		        			stack.pop();
		        			stack.pop();
		        			stack.pop();
		        			ingredientList.remove(floor);
		        			ingredientList.remove(floor-1);
		        			ingredientList.remove(floor-2);
		        			ingredientList.remove(floor-3);
		        			flag = true;
		        			break;
		        		}
		        		stack.push(ingredientList.get(floor));
		        		break;
		        		
		        	case 2:
		        		if (stack.size() == 0) {
		        			break;
		        		}
		        		if (stack.peek() == 1) {
		        			stack.push(ingredientList.get(floor));
		        		} else {
		        			stack.clear();
		        		}
		        		break;
		        		
		        	case 3:
		        		if (stack.size() == 0) {
		        			break;
		        		}
		        		if (stack.peek() == 2) {
		        			stack.push(ingredientList.get(floor));
		        		} else {
		        			stack.clear();
		        		}
		        		break;
		        }
	        	if (flag) {
	        		if (floor >= 3) {
	        			floor -= 3;
	        		} else {
	        			floor = 0;
	        		}
	        		flag = false;
	        	} else {
	        		floor ++;
	        	}
	        }
	        return answer;
	    }

	}
	
	public static void main(String[] args) {
		int[] ingr1 = {2, 1, 1, 2, 3, 1, 2, 3, 1};
		int[] ingr2 = {1, 3, 2, 1, 2, 1, 3, 1, 2};
		int[] ingr3 = {1, 2, 1, 2, 3, 1, 3, 1, 1, 2, 3, 1};
		int[] ingr4 = {1, 2, 3, 1, 2, 3, 1, 1, 1, 1, 2, 3, 1, 2, 3, 1, 1, 1, 1, 1, 1, 2, 3, 3, 1, 2, 3, 1, 3, 3, 3, 2, 1, 2, 3, 1};
		int[] ingr5 = {1, 2, 3, 1, 2, 3, 1, 1, 1, 1, 2, 3, 1, 2, 3, 1, 1, 1, 1, 1, 1, 2, 3, 3, 1};
		int[] ingr6 = {1, 2, 3, 1, 2, 3, 1, 1, 1, 1, 2, 3, 1, 2, 3, 1};
		int[] ingr7 = {1, 2, 1, 2, 3, 1, 3, 1, 2, 3, 1, 2, 3, 1};
		int[] ingr8 = {1, 2, 2, 3, 1};
		int[] ingr9 = {1,2,3,1,2,3,1,2,3,1,2,3,1};
		System.out.println(Solution.solution(ingr1));
		System.out.println(Solution.solution(ingr2));
		System.out.println(Solution.solution(ingr3));
		System.out.println(Solution.solution(ingr4));
		System.out.println(Solution.solution(ingr5));
		System.out.println(Solution.solution(ingr6));
		System.out.println(Solution.solution(ingr7));
		System.out.println(Solution.solution(ingr8));
		System.out.println(Solution.solution(ingr9));
	}

}
