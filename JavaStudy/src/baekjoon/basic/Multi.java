package baekjoon.basic;

import java.util.Scanner;

public class Multi {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        double A = in.nextDouble();
        double B = in.nextDouble();

        in.close();

        System.out.println(A/B);
    }
}
