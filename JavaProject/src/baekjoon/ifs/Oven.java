package baekjoon.ifs;

import java.util.Scanner;

public class Oven {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int hr = in.nextInt();
        int min = in.nextInt();
        int cook = in.nextInt();

        if (hr + ((min + cook) / 60) > 23) {
            hr = hr + ((min + cook) / 60) - 24;
            min = (min + cook) % 60;
        } else {
            hr = hr + ((min + cook) / 60);
            min = (min + cook) % 60;
        }
        System.out.print(hr);
        System.out.print(' ');
        System.out.print(min);
    }
}
