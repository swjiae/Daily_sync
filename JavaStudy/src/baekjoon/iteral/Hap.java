package baekjoon.iteral;

import java.util.Scanner;

public class Hap {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int num = in.nextInt();
        int hap = 0;
        for (int i=1; i<=num; i++) {
            hap += i;
        }
        System.out.println(hap);
    }
}
