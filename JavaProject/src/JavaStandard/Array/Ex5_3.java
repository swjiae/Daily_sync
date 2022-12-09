// 배열의 출력
    // 그냥 출력하면 참조변수 값을 출력
    // 예외) char[]는 값으로 출력
    // Arrays.toString 많이 사용 (클래스의 메서드)
package JavaStandard.Array;

import java.util.Arrays;

public class Ex5_3 {
    public static void main(String[] args) {
        int[] iArr = {1,2,3,4,5};

        // 배열을 출력하려면
        for(int i=0;i<iArr.length;i++) {
            System.out.println(iArr[i]);
        }

        // 메서드 활용
        System.out.println(Arrays.toString(iArr));
    }
}
