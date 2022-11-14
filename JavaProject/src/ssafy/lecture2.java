package ssafy;

// 배열

import java.util.Arrays;
import java.util.Random;

public class lecture2 {
    public static void main(String[] args) {
        int N = 6;
        Random rand = new Random();
        // 1 ~ 6 까지의 random 정수 5개를 저장할 배열을 만들고 값을 저장하시오.
        int [] arr = new int [5];
        for (int i=0; i<arr.length; i++) {
            arr[i] = rand.nextInt(N) +1;
        }
        System.out.println(Arrays.toString(arr));

        // 위 배열에 저장된 요소 중 짝수만 더해서 합을 출력하시오.
        int sum = 0;
        for (int i=0; i<arr.length; i++) {
            if (arr[i]%2 == 0) {
                sum += arr[i];
            }
        }
        System.out.println(sum);

        // char []을 이용해 String 'SSAFY'의 각 문자를 저장하고 출력하는 코드를 작성하시오.
        String org = "SSAFY";
        char [] chars = new char [org.length()];
        for (int i=0; i<org.length(); i++) {
            chars[i] = org.charAt(i);
        }
        System.out.println(Arrays.toString(chars));

        char [] byapi = org.toCharArray();
        System.out.println(Arrays.toString(byapi));

        // String "1234567890"의 자리 별 수를 1차원 배열에 저장하고 배열을 순회해서 그 합을 출력하시오.
        String num = "1234567890";
        char [] nums = num.toCharArray();

        int total = 0;
        for (int i=0; i<nums.length; i++) {
            total+=nums[i]-'0';
        }
        System.out.printf("total: %d%n", total);
    }
}
