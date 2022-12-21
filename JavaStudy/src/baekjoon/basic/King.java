package baekjoon.basic;

import java.util.Scanner;

public class King {
    public static void main(String[] args) {
        int [] piece = {1, 1, 2, 2, 2, 8};
        Scanner in = new Scanner(System.in);

        for (int i=0; i<piece.length; i++) {
            int A = in.nextInt();
            int result = piece[i] - A;
            System.out.print(result+" ");
        }
    }
}
