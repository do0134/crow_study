/*
 * 정확도 결과는 맞는데 효율성에서 틀린다
 * 당연하지... dfs로 풀었으니까...
 * 
 * 사유 : dfs는 모든 길이에 대해서 탐색해봐야 함 (완전탐색)
 * 그러나 bfs로 했으면 시작점에서 가까운 순서대로 탐색하게 되므로,
 * 목적지에 닿자마자 루트를 찾은 셈이 된다
 * 
 * 새로 발견한 거 : bfs할 때 방문배열 안 쓰고 지나온 자리를 1(벽)로 바꿔줘도 됨...
 * if문에 중복조건 걸지 않아도 됨
 * 
 * 궁금한 거 : 뎁스 카운트 어떻게 할 셈이지
 * 1. 큐의 크기를 재서 depth를 추론하기 (미심쩍)
 * 2. 방문배열을 int로 만들어서 depth를 기록하기 <-- 이걸 적용해서 새로 풀어보기
 *
 * 신경썼던 거 : M, N까지는 영원히 못 다다른다... 당연함 크기가 안맞음
 * M-1, N-1까지 닿으면 종료
 */

import java.lang.Math;

class Solution {
    static int M;
    static int N;
    static boolean[][] visited;
    static int[][] map;
    static int COUNT = Integer.MAX_VALUE;
    static int[] dr = {-1,0,1,0};
    static int[] dc = {0,1,0,-1};
    
    public int solution(int[][] maps) {
        
        M = maps.length;
        N = maps[0].length;
        
        visited = new boolean[M][N];
        map = maps;
        
        dfs(0,0,1);
        
        // 여기서 현재 위치랑 그간의 누적값을 갖는 dfs를 돌려보자
        if(COUNT==Integer.MAX_VALUE) {
            return -1;
        }
        
        // 그걸 돌린 결과가 COUNT에 저장되어 있음
        int answer = COUNT;
        return answer;
    }
    
    static boolean check(int x, int y, int r, int c){
        return x+r>=0 && y+c>=0 && x+r<M && y+c<N;
    }
    
    static void dfs(int x, int y, int count){
        
        visited[x][y] = true;
        
        if(x==M-1 && y==N-1) {
            COUNT = Math.min(count, COUNT);
            return;
        }
        
        for(int d=0;d<4;d++){
            if(check(x, y, dr[d], dc[d]) && !visited[x+dr[d]][y+dc[d]] && map[x+dr[d]][y+dc[d]]==1){
                dfs(x+dr[d], y+dc[d], count+1);
                visited[x+dr[d]][y+dc[d]] = false;
            }
        }
        
    }

}

// static으로 맵 크기 받아두기
// 재귀함수로 다녀오기
// 방문배열을 만들어서 관리하면 좀 덜 가려나? <- 돌아올 때는 방금 전에 갔던 체크를 해제하는 걸로...?
// 카운트 하나씩 세면서 감
// 특정 위치에 갔을 때 카운트를 비교함
