package ssafy;

// 기본

public class lecture1 {
    public static void main(String[] args) {
        // hello world
        System.out.println("Hello world!");

        // overflow
        int i1 = Integer.MAX_VALUE;
        int i2 = i1+1;
        System.out.println(i2);

        int i3 = 1000000 * 1000000 / 1000000;
        int i4 = 1000000 / 1000000 * 1000000;
        System.out.println(i3 + ":" + i4);

        // 형변환
        long l1 = (long)i1+1;
        System.out.println(l1);

        // 연산자 &
        int a = 10;
        int b = 20;
        System.out.println((a > b) & (b > 0));

        // 연산자 |
        System.out.println((a += 10) > 15 | (b -= 10) > 15);
        System.out.println("a:" + a + "b:" + b);

        // 연산자 ||
        int c = 10;
        int d = 20;
        System.out.println((c += 10) > 15 || (d -= 10) > 15);
        System.out.println("a:" + c + "b:" + d);
    }
}
