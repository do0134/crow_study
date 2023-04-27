// 시간초과, 이거 아마 값 저장해가면서 DP.. 문제인 것 같다
// BOJ 2169 로봇 조종하기
// https://www.acmicpc.net/problem/2169

package al_0427;

import java.util.Scanner;

public class boj_2169 {
	static int n;
	static int m;
	static int[][] arr;
	static int[][] dd = {{0, 1}, {1, 0}, {0, -1}};
	static boolean[][] visited;
	static int maxx = 0;
	
	public static void DFS(int x, int y, int summ) {
		if (x == n-1 && y == m-1) {
			if (maxx < summ) {
				maxx = summ;
				return;
			}
		}
		for (int[] dxdy : dd) {
			int nx = x + dxdy[0];
			int ny = y + dxdy[1];
			if (0 <= nx && nx < n && 0 <= ny && ny < m && !visited[nx][ny]) {
				visited[nx][ny] = true;
				DFS(nx, ny, summ + arr[nx][ny]);
				visited[nx][ny] = false;
			}
		}
	}
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		n = scanner.nextInt();
		m = scanner.nextInt();
		arr = new int[n][m];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				arr[i][j] = scanner.nextInt();
			}
		}
		visited = new boolean[n][m];
		visited[0][0] = true;
		DFS(0, 0, arr[0][0]);
		System.out.println(maxx);
	}

}
