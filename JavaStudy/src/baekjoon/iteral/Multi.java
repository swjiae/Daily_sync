package baekjoon.iteral;

import java.util.Scanner;

public class Multi {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int num = in.nextInt();

        for (int i=1; i<10; i++) {
            System.out.printf("%d * %d = %d%n", num, i, num*i);
        }
    }
}
