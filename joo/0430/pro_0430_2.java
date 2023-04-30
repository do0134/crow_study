// programmers 연습문제 - 호텔 대실
// https://school.programmers.co.kr/learn/courses/30/lessons/155651?language=java

package al_0430;

import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class pro_0430_2 {

	class Solution {
	    public int time_change(String time) {
	        String[] times = time.split(":");
	        return Integer.parseInt(times[0]) * 60 + Integer.parseInt(times[1]);
	    }
	    public int solution(String[][] book_time) {
	        int answer = 0;
	        List<int[]> rooms = new ArrayList<>();
	        for (String[] books: book_time) {
	            int[] start = {time_change(books[0]), 0};
	            int[] end = {time_change(books[1]) + 10, 1};
	            rooms.add(start); rooms.add(end);
	        }
	        Collections.sort(rooms, (a, b) -> {
	            if (a[0] > b[0]) return 1;
	            else if (a[0] < b[0]) return -1;
	            else {
	                if (a[1] > b[1]) return -1;
	                else return 1;
	            }
	        });
	        int now = 0;
	        for (int[] room : rooms) {
	            if (room[1] == 0) {
	                now += 1;
	            } else {
	                now -= 1;
	            }
	            if (answer < now) {
	                answer = now;
	            }
	        }
	        return answer;
	    }
	}

}
