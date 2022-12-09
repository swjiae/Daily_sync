// String 배열

package JavaStandard.Array;

public class Ex5_5 {
    public static void main(String[] args) {
        String[] strArr = {"가위", "바위", "보"};

        for (int i=0; i<10; i++) {
            int tmp = (int)(Math.random()*3);
            System.out.println(strArr[tmp]);
        }
    }
}
