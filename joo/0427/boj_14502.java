// BOJ 14502 연구소
// https://www.acmicpc.net/problem/14502


package al_0427;

import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.ArrayDeque;
import java.util.Deque;


public class boj_14502 {
	static int n;
	static int m;
	static String[][] arr;
	static int[][] dd = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
	static int maxx = 0;
	// 벽 3개 세우기
	public static void DFS(int depth) {
		if (depth == 3) {
			BFS();
			return;
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (Integer.parseInt(arr[i][j]) == 0) {
					arr[i][j] = "1";
					DFS(depth + 1);
					arr[i][j] = "0";
				}
			}
		}
	}
	
	// 바이러스 퍼지기
	public static void BFS() {
		Deque<int[]> queue = new ArrayDeque<>();
		int[][] virus = new int[n][m];
		
		// 복제
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				virus[i][j] = Integer.parseInt(arr[i][j]);
			}
		}
		
		// 바이러스 찾기
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (Integer.parseInt(arr[i][j]) == 2) {
					int[] tmp = {i, j};
					queue.add(tmp);
				}
			}
		}
		// 바이러스 퍼지기
		while (!queue.isEmpty()) {
			int[] now = queue.removeFirst();
			for (int[] dxdy : dd) {
				int nx = now[0] + dxdy[0];
				int ny = now[1] + dxdy[1];
				if (0 <= nx && nx < n && 0 <= ny && ny < m && virus[nx][ny] == 0) {
					virus[nx][ny] = 2;
					int[] tmp = {nx, ny};
					queue.add(tmp);
				}
			}
		}
		safe(virus);
		return;
		
	}
	
	public static void safe(int[][] map) {
		int cnt = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (map[i][j] == 0) {
					cnt += 1;
				}
			}
		}
		if (cnt > maxx) {
			maxx = cnt;
		}
		return;
	}

	public static void main(String[] args) {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		try {
			String[] tmp = reader.readLine().split(" ");
			n = Integer.parseInt(tmp[0]);
			m = Integer.parseInt(tmp[1]);
			arr = new String[n][m];
			for (int i = 0; i < n; i++) {
				arr[i] = reader.readLine().split(" ");
			}
		} catch(IOException e) {
			new RuntimeException(e);
		}
		// 벽을 세울 세 좌표 정해서 bfs 함수 사용
		DFS(0);
		System.out.println(maxx);
		
	}
}
