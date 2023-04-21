// BOJ 10799 쇠막대기
// https://www.acmicpc.net/problem/10799

package al_0421;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayDeque;
import java.util.Deque;


public class boj_10799 {
	public static int metal(List<String> strings) {
		int ans = 0;
		Deque<String> deque = new ArrayDeque<>();
		int i = 0;
		while (i < strings.size()-1) {
			// 레이저인 경우
			if (strings.get(i).equals("(") && strings.get(i+1).equals(")")) {
				ans += deque.size();
				i += 2;
			}
			else if (strings.get(i).equals("(")) {
				deque.addLast("(");
				i++;
			}
			else {
				deque.removeLast();
				ans += 1;
				i++;
			}
		}
		ans += deque.size()
;		return ans;
	}
	
	public static void main(String[] args) {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		List<String> strings = new ArrayList<>();
		try {
			strings = Arrays.asList(reader.readLine().split(""));
		} catch (IOException e) {
			new RuntimeException(e);
		}
		System.out.println(metal(strings));
	}

}
