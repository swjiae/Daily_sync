package baekjoon.basic;

import java.util.Scanner;

public class Multi2 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        int b = in.nextInt();

        int c1 = b % 10;
        System.out.println(a*c1);
        int c2 = b / 10 % 10;
        System.out.println(a*c2);
        int c3 = b / 100 % 10;
        System.out.println(a*c3);
        System.out.println(a*b);
    }
}