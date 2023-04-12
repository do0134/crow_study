//https://school.programmers.co.kr/learn/courses/30/lessons/72410

package algorithm;

public class pro_newid {
	
	public static String solution(String new_id) {
        String answer = "";
        new_id = new_id.toLowerCase();
        new_id = new_id.replaceAll("[^\\w.-]","");
//        System.out.println(new_id);
        new_id = new_id.replaceAll("\\.+", ".");
//        System.out.println(new_id);
        if (new_id.length() > 0 && new_id.charAt(0) == '.') { new_id = new_id.substring(1); }
//        System.out.println(new_id);
        if (new_id.length() > 0 && new_id.charAt(new_id.length()-1) == '.') { new_id = new_id.substring(0, new_id.length() - 1); }
//        System.out.println(new_id);
        if (new_id.length() == 0) { new_id = "a"; }
        if (new_id.length() >= 16) { new_id = new_id.substring(0,15); }
//        System.out.println(new_id);
        if (new_id.charAt(new_id.length()-1) == '.') { new_id = new_id.substring(0, new_id.length()-1); }
        if (new_id.length() <= 2) {
            while (new_id.length() < 3) {
                new_id = new_id + (new_id.charAt(new_id.length()-1));
            }
        }
//        System.out.println(new_id);
        answer = new_id;
        return answer;
    }
	
	public static void main(String[] args) {
		System.out.println("hello");
		System.out.println(solution("...!@BaT#*..y.abcdefghijklm"));
	}
}
