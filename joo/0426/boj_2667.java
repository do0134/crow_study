// BOJ 2667 단지번호붙이기
// https://www.acmicpc.net/problem/2667

package al_0426;

import java.util.ArrayList;
import java.util.List;
import java.util.Collections;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;

public class boj_2667 {
	static int n;
	static String[][] arr;
	static List<Integer> ans = new ArrayList<>();
	static boolean[][] visited;
	static int maxx = 0;
	static int[][] dd = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
	public static void DFS(int x, int y) {
		visited[x][y] = true;
		maxx += 1;
		for (int[] dxdy : dd) {
			int nx = x + dxdy[0];
			int ny = y + dxdy[1];
			if (0 <= nx && nx < arr.length && 0 <= ny && ny < arr.length && arr[nx][ny].equals("1") && !visited[nx][ny]) {
				DFS(nx, ny);
			}
		}
		
	}
	
	public static void main(String[] args) {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		try {
			n = Integer.parseInt(reader.readLine());
		} catch(IOException e) {
			new RuntimeException(e);
		}
		arr = new String[n][n];
		try {
			for (int i = 0; i < n; i++) {
				arr[i] = reader.readLine().split("");
			}
		} catch(IOException e) {
			new RuntimeException(e);
		}
		visited = new boolean[n][n];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (arr[i][j].equals("1") && !visited[i][j]) {
					DFS(i, j);
					ans.add(maxx);
					maxx = 0;
				}
			}
		}
		Collections.sort(ans);
		System.out.println(ans.size());
		for (int x : ans) {
			System.out.println(x);
		}
	}

}
