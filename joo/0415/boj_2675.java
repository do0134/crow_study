// boj 2675 문자열 반복
// https://www.acmicpc.net/problem/2675

package al_0415;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.List;
import java.util.ArrayList;


public class boj_2675 {
	public static void repeat(int t, List<String[]> strings) {
		for (int i = 0; i < t; i++) {
			String str = "";
			for (int j = 0; j < strings.get(i)[1].length(); j++) {
				for (int h = 0; h < Integer.parseInt(strings.get(i)[0]); h++) {
					str += strings.get(i)[1].substring(j, j+1);
				}
			}
			System.out.println(str);
		}
	}

	public static void main(String[] args) {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		List<String[]> strings = new ArrayList<>();
		int t = 0;
		try {
			t = Integer.parseInt(reader.readLine());
			for (int i = 0; i < t; i ++) {
				strings.add(reader.readLine().split(" "));
			}
		} catch(IOException e) {
			new RuntimeException(e);
		}
		repeat(t, strings);
		
	}
}
