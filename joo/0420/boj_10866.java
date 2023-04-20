// BOJ 10866 덱
// https://www.acmicpc.net/problem/10866

package al_0420;

import java.util.ArrayDeque;
import java.util.Deque;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.List;
import java.util.ArrayList;

public class boj_10866 {
	public static List<String> mkdq(int n, List<String[]> lst) {
		Deque<String> queue = new ArrayDeque<>();
		List<String> ans = new ArrayList<>();
		for (int i = 0; i < n; i++) {
			switch (lst.get(i)[0]) {
			case "push_front":
				queue.addFirst(lst.get(i)[1]);
				break;
			
			case "push_back":
				queue.addLast(lst.get(i)[1]);
				break;
				
			case "pop_front":
				if (queue.size() != 0) {
					ans.add(queue.removeFirst());
				} else {
					ans.add("-1");
				}
				break;
				
			case "pop_back":
				if (queue.size() != 0) {
					ans.add(queue.removeLast());
				} else {
					ans.add("-1");
				}
				break;
				
			case "size":
				ans.add(Integer.toString(queue.size()));
				break;
				
			case "empty":
				if (queue.size() == 0) {
					ans.add("1");
				} else {
					ans.add("0");
				}
				break;
			
			case "front":
				if (queue.size() != 0) {
					ans.add(queue.getFirst());
				} else {
					ans.add("-1");
				}
				break;
				
			case "back":
				if (queue.size() != 0) {
					ans.add(queue.getLast());
				} else {
					ans.add("-1");
				}
				break;
			}
			
		}
		return ans;
	}

	public static void main(String[] args) {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		List<String[]> strings = new ArrayList<>();
		int n;
		try {
			n = Integer.parseInt(reader.readLine());
		} catch (IOException e) {
			throw new RuntimeException(e);
		}
		try {
			for (int i = 0; i < n; i++) {
				String[] str = reader.readLine().split(" ");
				strings.add(str);
			}
		} catch (IOException e) {
			throw new RuntimeException(e);
		}
		List<String> ans = mkdq(n, strings);
		for (int i = 0; i < ans.size(); i++) {
			System.out.println(ans.get(i));
		}
		
	}
}
