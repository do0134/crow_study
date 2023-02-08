/*
 * 테케는 통과했는데 통과를 못함...
 * ㅜㅜ 원본배열 손 안댔는데 왜...
 * BFS로 해결
 */

import java.lang.Math;
import java.util.LinkedList;
import java.util.Queue;

class Solution {
    
    static int MAX;
    static int COUNT;
    static int[] dr = {-1,0,1,0};
    static int[] dc = {0,1,0,-1};
    static boolean[][] visited;
    static int M;
    static int N;
    
    public static class Now {
        int r;
        int c;
        
        public Now(int r, int c){
            this.r = r;
            this.c = c;
        }
    }
    
    public static int[] solution(int m, int n, int[][] picture) {
        
        MAX = 0;
        COUNT = 0;        
        M = m;
        N = n;
        visited = new boolean[m][n];
        
        int[] answer = new int[2];
        answer[0] = COUNT;
        answer[1] = MAX;
        
        int[][] arr = new int[M][N];
        
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                arr[i][j] = picture[i][j];
            }
        }
        
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(arr[i][j]==0){
                    // 0이니까 bfs 돌리지 않고 방문 체크만 함
                    visited[i][j] = true;
                } else {
                    if(!visited[i][j]){
                        // 0이 아니고, 방문한 적 없음
                        visited[i][j] = true;
                        Queue<Now> que = new LinkedList<>();
                        Now now = new Now(i, j);
                        que.offer(now);
                        bfs(que, arr[i][j], arr);
                        COUNT++;
                    }
                }
       
            }
        }

        answer[0] = COUNT;
        answer[1] = MAX;
        return answer;
    }
    
    static void bfs(Queue<Now> que, int color, int[][] arr) {
        int max = 0;
        
        while(!que.isEmpty()) {
            max++;
            Now now = que.poll();
            int rr = now.r;
            int cc = now.c;
            
            for(int d=0;d<4;d++){
                if(check(rr,cc,dr[d],dc[d]) && !visited[rr+dr[d]][cc+dc[d]]){
                    // 가도 되는 곳이고 아직 가본 적 없음
                    visited[rr+dr[d]][cc+dc[d]] = true;
                    if(arr[rr+dr[d]][cc+dc[d]]==color){
                        // 색도 같으면 다음 탐색 범위에 집어넣음
                        Now temp = new Now(rr+dr[d], cc+dc[d]);
                        que.offer(temp);
                    }
                }

            }
        }
        
        MAX = Math.max(MAX, max);
    }
        
        
    static boolean check(int x, int y, int r, int c){
        return x+r>=0 && y+c>=0 && x+r<M && y+c<N;
    }
    
}
