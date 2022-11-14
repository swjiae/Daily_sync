package ssafy.day1;

import java.util.Arrays;
import java.util.Random;

public class Array1 {
    public static void main(String[] args) {
        int N = 6;
        Random rand = new Random();

        // 1. 1~5 까지의 random 정수 5개를 저장할 배열을 만들고 값을 저장하시오.
        int [] arr = new int [5]; // 1) 선언 (int의 배열 arr) 2) 메모리 구성 3) 할당
        for (int i=0; i<arr.length; i++) {
            arr[i] = rand.nextInt(N);
        }
        System.out.println(Arrays.toString(arr));

        // 2. 위 배열에 저장된 요소 중 짝수만 더해서 합을 출력하시오.
        int sum = 0;
        for(int i=0; i<arr.length; i++) {
            if(arr[i]%2==0) {
                sum+=arr[i];
            }
        }
        System.out.println(sum);

        // 3. char []을 이용해 String 'SSAFY'의 각 문자를 저장하고 출력하는 코드를 작성하시오.

            // for 문을 활용한 방법
            String org = "SSAFY";
            char [] chars = new char[org.length()]; // 문자열이 가진 length() 메서드
            for(int i=0; i<chars.length; i++) {
                chars[i] = org.charAt(i); // charAt(index) 문자열에서 해당하는 인덱스의 문자를 반환하는 메서드
            }
            System.out.println(Arrays.toString(chars));

            // 메서드를 활용한 방법
            char [] chars2 = org.toCharArray(); // toCharArray 를 통해 string을 array로 변환
            System.out.println(Arrays.toString(chars2));

        // 4. String "1234567890"의 자리 별 수를 1차원 배열에 저장하고 배열을 순회해서 그 합을 출력하시오.
        String nums = "1234567890";
        char [] nrr = nums.toCharArray();
        int total = 0;
        for(int i=0; i<nrr.length; i++) {
            total+=nrr[i]-'0'; // java에서 산술의 최소단위는 int
        }
        System.out.printf("sum: %d%n", sum);
    }
}
