//
// 배열의 인덱스배열의 선언과 생성

package JavaStandard.Array;

import java.util.Arrays;

public class Ex5_1 {
    public static void main(String[] args) {
//        int[] score; // 1. 배열 score를 선언 (참조변수)
//        score = new int[5]; // 2. 배열의 생성 (int저장공간*5) 및 할당

        int[] score = new int[5]; // 배열의 선언과 생성을 동시에
        score[3] = 100;
        System.out.println(score[3]);
    }
}
