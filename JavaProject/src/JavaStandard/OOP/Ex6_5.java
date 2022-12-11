// 생성자 this()

package JavaStandard.OOP;

public class Ex6_5 {
}

class Car2 {
    String color;
    String gearType;
    int door;

    // 기본생성자 (default iv)
    // Car2() {
    //     color = "white";
    //     gearType = "auto";
    //     door = 4;
    // }

    // 중복을 제거한 기본 생성자
    Car2() {
        this("white", "auto", 4);
    }

    Car2(String c, String g, int d) {
        color = c;
        gearType = g;
        door = d;
    }
}
