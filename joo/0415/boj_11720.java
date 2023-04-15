// boj 11720 숫자의 합
// https://www.acmicpc.net/problem/11720

package al_0415;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.List;
import java.util.ArrayList;

public class boj_11720 {
	public static int plus(int n, String num) {
		int answer = 0;
		for (int i = 0; i < n; i++) {
			answer += Integer.parseInt(num.substring(i, i+1));
		}
		return answer;
	}
	public static void main(String[] args) {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		List<String> strings = new ArrayList<>();
		try {
			String str;
			for (int i = 0; i < 2; i++) {
				strings.add(reader.readLine());
			}
		} catch (IOException e) {
			throw new RuntimeException(e);
		}
		System.out.println(plus(Integer.valueOf(strings.get(0)), strings.get(1)));
	}
}
