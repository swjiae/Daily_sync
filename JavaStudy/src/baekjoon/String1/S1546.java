package baekjoon.String1;

import java.util.Scanner;

public class S1546 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int[] scores = new int[N];
        int Max = 0;
        for (int i=0; i<N; i++) {
            scores[i] = in.nextInt();
            if (Max < scores[i]) {
                Max = scores[i];
            }
        }

        double total = 0;
        for (double score:scores) {
             total += score/Max*100;
        }
        double result = total/N;

        System.out.println(result);

    }
}
