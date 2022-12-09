// 배열의 활용
    // 총합, 평균
    // 최대, 최소
    // 자리 바꾸기

package JavaStandard.Array;

import java.util.Arrays;

public class Ex5_4 {
    public static void main(String[] args) {
        // 총합, 평균
        int sum = 0;
        float average = 0f;

        int[] score = {100,88,100,100,90};

        for (int i=0; i<score.length; i++) {
            sum += score[i];
        }
        average = sum/(float)score.length;

        System.out.println(average);

        // 최대, 최소
        int max = score[0];
        int min = score[0];

        for (int i=1; i<score.length; i++) {
            if (max < score[i]) {
                max = score[i];
            }
            if (min > score[i]) {
                min = score[i];
            }
        }
        System.out.println(max);
        System.out.println(min);

        // 자리 바꾸기
        System.out.println(Arrays.toString(score));
        int tmp = score[0];
        score[0] = score[1];
        score[1] = tmp;
        System.out.println(Arrays.toString(score));

        // 로또 번호 뽑기
        int[] ball = new int[45];

        for (int i=0; i<ball.length; i++) {
            ball[i] = i+1;
        }

        int tmp2 = 0;
        int j = 0;

        for (int i=0; i<6; i++) {
            j = (int)(Math.random()*45);
            tmp2 = ball[i];
            ball[i] = ball[j];
            ball[j] = tmp2;
        }

        for (int i=0; i<6; i++){
            System.out.println(ball[i]);
        }
    }
}
