package baekjoon.String1;

import java.util.Scanner;

public class S8958 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int T = in.nextInt();
        for (int t=0; t<T; t++) {
            String str = in.next();

            int score = 0;
            int seq = 1;
            char pre = 'X';
            for (char c: str.toCharArray()) {
                if (c == 'O') {
                    if (pre == 'O'){
                        seq ++;
                    }
                    score += seq;
                } else {
                    seq = 1;
                }
                pre = c;
            }
            System.out.println(score);
        }
    }
}
