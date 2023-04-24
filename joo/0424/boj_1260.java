// BOJ 1260 DFS와 BFS
// https://www.acmicpc.net/problem/1260

package al_0424;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.ArrayDeque;

public class boj_1260 {
	static boolean[] visited;
	static String sd = "";
	static int[][] arr;
	public static void DFS(int now) {
		visited[now] = true;
		sd += Integer.toString(now)+ " ";
		for (int i = 1; i < arr.length; i++) {
			if (arr[now][i] == 1 && !visited[i]) {
				DFS(i);
			}
		}
	}
	
	static String sb = "";
	public static void BFS(int start) {
		Deque<Integer> queue = new ArrayDeque<>();
		queue.add(start);
		while (!queue.isEmpty()) {
			int now = queue.removeFirst();
			if (visited[now]) {
				continue;
			}
			visited[now] = true;
			sb += Integer.toString(now) + " ";
			for (int i = 1; i < arr.length; i++) {
				if (arr[now][i] == 1 && !visited[i]) {
					queue.addLast(i);
				}
			}
		}
	}

	public static void main(String[] args) {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		String[] first = new String[3];
		try {
			first = reader.readLine().split(" ");
		} catch (IOException e) {
			new RuntimeException(e);
		}
		int N = Integer.parseInt(first[0]);
		int M = Integer.parseInt(first[1]);
		int V = Integer.parseInt(first[2]);
		arr = new int[N+1][N+1];
		visited = new boolean[N+1];
		try {
			for (int i = 0; i < M; i++) {
				String[] strings = reader.readLine().split(" ");
				arr[Integer.parseInt(strings[0])][Integer.parseInt(strings[1])] = 1;
				arr[Integer.parseInt(strings[1])][Integer.parseInt(strings[0])] = 1;
			}
		} catch (IOException e) {
			new RuntimeException(e);
		}
		visited = new boolean[N+1];
		DFS(V);
		visited = new boolean[N+1];
		BFS(V);
		System.out.println(sd.strip());
		System.out.println(sb.strip());
	}
}
