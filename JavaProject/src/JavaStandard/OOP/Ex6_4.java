// constructor with parameter

package JavaStandard.OOP;

public class Ex6_4 {
    public static void main(String[] args) {
        Car c = new Car("white", "auto", 4);
        // Car c : 참조변수 선언
        // new : 객체 생성
        // Car() : 객체 초기화
    }
}

class Car {
    String color;
    String gearType;
    int door;

    // 기본 생성자
    Car() {}
    // 매개변수가 있는 생성자
    Car(String c, String g, int d) {
        color = c;
        gearType = g;
        door = d;
    }
}
