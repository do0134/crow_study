// boj 7576 토마토
// https://www.acmicpc.net/problem/7576


package al_0427;

import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.List;
import java.util.ArrayList;

public class boj_7576 {
	static int n;
	static int m;
	static String[][] arr;
	static int[][] visited;
	static int[][] dd = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
	
	public static int BFS(List<int[]> tomato) {
		int ans = 0;
		Deque<int[]> queue = new ArrayDeque<>();
		for (int[] xy : tomato) {
			queue.add(xy);
			visited[xy[0]][xy[1]] = 1;
		}
		while (queue.size() != 0) {
			int[] tmp = queue.removeFirst();
			for (int[] dxdy : dd) {
				int nx = tmp[0] + dxdy[0];
				int ny = tmp[1] + dxdy[1];
				if (0 <= nx && nx < n && 0 <= ny && ny < m && arr[nx][ny].equals("0") && visited[nx][ny] == 0) {
					int[] nxny = {nx, ny};
					queue.add(nxny);
					visited[nx][ny] = visited[tmp[0]][tmp[1]] + 1;
					if (ans < visited[nx][ny]) {
						ans = visited[nx][ny];
					}
				}
			}
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j< m; j++) {
				if (visited[i][j] == 0 && !arr[i][j].equals("-1")) {
					ans = -1;
					break;
				}
			}
		}
		if (ans > 0) {
			ans -= 1;
		}
		return ans;
	}

	public static void main(String[] args) {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		try {
			String[] tmp = reader.readLine().split(" ");
			m = Integer.parseInt(tmp[0]);
			n = Integer.parseInt(tmp[1]);
			arr = new String[n][m];
			for (int i = 0; i < n; i++) {
				arr[i] = reader.readLine().split(" ");
			}
		} catch(IOException e) {
			new RuntimeException(e);
		}
		visited = new int[n][m];
		List<int[]> tomato = new ArrayList<>();
		for (int i = 0; i < n; i++) {
			for (int j = 0; j< m; j++) {
				if (arr[i][j].equals("1")) {
					int[] tmp = {i, j};
					tomato.add(tmp);
				}
			}
		}
		System.out.println(BFS(tomato));
	}
}
