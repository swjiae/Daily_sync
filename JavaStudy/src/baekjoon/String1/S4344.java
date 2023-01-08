package baekjoon.String1;

import java.util.Scanner;

public class S4344 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int T = in.nextInt();
        for (int t=0; t<T; t++) {
            // 배열 입력받기
            int N = in.nextInt();
            int[] scores = new int[N];
            double total = 0;
            for (int i = 0; i < N; i++) {
                scores[i] = in.nextInt();
                // 반 점수 총 합 구하기
                total += scores[i];
            }
            // 반 점수 평균 구하기
            double avg = total / N;

            // 평균 넘는 학생 수 구하기
            double cnt = 0;
            for (int score : scores) {
                if (score > avg) {
                    cnt += 1;
                }
            }

            // 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력
            double result = cnt / N * 100;
            System.out.printf("%.3f%%\n", result);
        }
    }
}

