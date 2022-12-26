package baekjoon.String1;

import java.util.Scanner;

public class S5597 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int[] checkList = new int[31];

        for (int i=0; i<28; i++) {
            int attend = in.nextInt();
            checkList[attend] = 1;
        }

        for (int i=1; i<=30; i++) {
            if (checkList[i] != 1) {
                System.out.println(i);
            }
        }

    }
}
