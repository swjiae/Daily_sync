package baekjoon.ifs;

import java.util.Scanner;

public class Alam {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int hr = in.nextInt();
        int min = in.nextInt();

        if ((hr == 0) && (min < 45)) {
            hr = 23;
            min = 60 + min - 45;
        } else if (min < 45) {
            hr -= 1;
            min = 60 + min - 45;
        } else {
            min -= 45;
        }
        System.out.print(hr);
        System.out.print(' ');
        System.out.print(min);
    }
}