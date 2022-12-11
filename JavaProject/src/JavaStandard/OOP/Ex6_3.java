// basic constructor

package JavaStandard.OOP;

public class Ex6_3 {
    public static void main(String[] args) {
        Data_1 d1 = new Data_1();
        Data_2 d2 = new Data_2();
    }
}

class Data_1 {
    int value;
}

class Data_2 {
    int value;
    Data_2() {}
    // 매개변수가 있는 생성자
    Data_2(int x) {
        value = x;
    }
}

