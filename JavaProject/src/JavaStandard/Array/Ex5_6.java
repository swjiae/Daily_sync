// 2차원 배열의 선언과 생성
    // int[][] score = new int[행][열];
// 2차원 배열의 초기화
    // int[][] score = {{1,2}, {3,4}};

package JavaStandard.Array;

public class Ex5_6 {
    public static void main(String[] args) {
        int[][] score = {
                {100, 100, 100},
                {20, 20, 20},
                {30, 30, 30},
                {40, 40, 40}
        };
        int sum = 0;

        for (int i=0; i<score.length; i++) {
            for (int j=0; j<score[i].length; j++) {
                sum += score[i][j];
            }
        }
        System.out.println(sum);
    }
}
