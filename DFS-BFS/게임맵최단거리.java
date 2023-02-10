/*
 * bfs로 풀어서 해결함!!
 * 
 * 사유 : dfs는 모든 길이에 대해서 탐색해봐야 함 (완전탐색)
 * 그러나 bfs로 했으면 시작점에서 가까운 순서대로 탐색하게 되므로,
 * 목적지에 닿자마자 루트를 찾은 셈이 된다
 * 
 * 새로 발견한 거 : bfs할 때 방문배열 안 쓰고 지나온 자리를 1(벽)로 바꿔줘도 됨...
 * if문에 중복조건 걸지 않아도 됨
 * 
 * 뎁스 카운트한 방법 : 방문배열을 int로 만들어서 depth를 기록하기
 * 시작점을 1로
 * 도착점인지를 확인하는 부분에 갔을 땐 이미 그 칸의 방문배열이 체크된 상태이므로 그대로 출력
 *
 * 신경썼던 거 : M, N까지는 영원히 못 다다른다... 당연함 크기가 안맞음
 * M-1, N-1까지 닿으면 종료
 */

import java.lang.Math;
import java.util.LinkedList;
import java.util.Queue;

class Solution {
    static int M;
    static int N;
    static int[][] visited;
    static int[][] map;
    static int COUNT = Integer.MAX_VALUE;
    static int[] dr = {-1,0,1,0};
    static int[] dc = {0,1,0,-1};
    
    class Now{
        int x;
        int y;
        
        public Now(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
    
    public int solution(int[][] maps) {
        
        M = maps.length;
        N = maps[0].length;
        
        visited = new int[M][N];
        map = maps;
        
        Queue<Now> que = new LinkedList<>();
        
        que.offer(new Now(0,0));
        visited[0][0] = 1;
        
        while(!que.isEmpty()){
            Now temp = que.poll();
            int x = temp.x;
            int y = temp.y;
            
            if(x==M-1 && y==N-1){
                return visited[x][y];
            }
            
            for(int d=0;d<4;d++){
                
                int nx = x+dr[d];
                int ny = y+dc[d];
                
                if(check(nx, ny) && visited[nx][ny]==0 && map[nx][ny]==1) {
                    // 갈 수 있는 곳이고 && 방문한 적 없고 && 갈 수 있는 길임
                    visited[nx][ny] = visited[x][y]+1;
                    que.offer(new Now(nx, ny));
                }  
                
            }

        }
        
        return -1;
 
        
    }
    
    static boolean check(int x, int y){
        return x>=0 && y>=0 && x<M && y<N;
    }

}

// bfs로 풀이함
