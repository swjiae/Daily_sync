// 배열의 길이
    // 배열이름.length
    // 배열은 한 번 생성하면 실행하는 동안 그 길이를 바꿀 수 없다.
        // 왜? 연속되어야하는데 뒤에 공간이 없으면?
        // 부족하면? 새로 만들고 기존 내용 복붙
// 배열의 초기화
    // 배열의 각 요소에 처음으로 값을 저장하는 것
    // int[] score = new int[]{1,2,3,4,5};
    // int[] score = {1,2,3,4,5}; 두 줄로 나누면 안 됨
package JavaStandard.Array;

public class Ex5_2 {
    public static void main(String[] args) {
    int[] arr = new int[5];
    System.out.println(arr.length);

    for(int i=0;i<arr.length;i++) {
        System.out.println(arr[i]);
    }
    }
}
