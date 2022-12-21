package baekjoon.ifs;

import java.util.Scanner;

public class Yoon {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int year = in.nextInt();

        if (year % 4 == 0 && year % 100 != 0 || year % 400 == 0) {
            System.out.print(1);
        } else {
            System.out.print(0);
        }
    }
}
