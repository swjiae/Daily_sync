package baekjoon.String1;

import java.util.Scanner;

public class S2562 {
    public static void main(String[] args) {
        int[] arr = new int[9];
        Scanner in = new Scanner(System.in);
        for (int i=0; i<9; i++) {
            arr[i] = in.nextInt();
        }

        int max = 0;
        int idx = 0;
        for (int i=0; i<9; i++) {
            if (arr[i] > max) {
                max = arr[i];
                idx = i+1;
            }
        }

        System.out.println(max);
        System.out.println(idx);
    }
}
