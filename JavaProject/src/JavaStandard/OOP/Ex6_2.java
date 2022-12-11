// overloading

package JavaStandard.OOP;

public class Ex6_2 {
    public static void main(String[] args) {

    }
}

class MyMath3 {
    int add(int a, int b) {
        return a+b;
    }

    long add(long a, long b) {
        return a+b;
    }

    int add(int[] a) {
        int result = 0;
        for (int i=0; i<a.length; i++) {
            result += a[i];
        }
        return result;
    }
}