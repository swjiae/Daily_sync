package baekjoon.basic;

// 1. Scanner 클래스를 import
import java.util.Scanner;

public class Plus {
    public static void main(String[] args) {
        // 2. 객체 생성
            // Scanner 객체명 = new Scanner(System.in);
            // 객체명은 보통 in, scan, sc 사용
        Scanner in = new Scanner(System.in);
        int A = in.nextInt();
        int B = in.nextInt();

        System.out.println(A+B);

        in.close();
    }
}
