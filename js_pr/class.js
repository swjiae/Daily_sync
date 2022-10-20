// 클래스 생성
class Person {
  // 인스턴스 생성할 때 호출되는 함수 (생성자)
  constructor(name, age) {
    // 인스턴스 변수
    this.name = name
    this.age = age
  }
	// 메서드 생성
	intro() {
		console.log(`My name is ${this.name}.`)
	}
}

// 인스턴스 생성
const person1 = new Person('David', 35)

// 인스턴스 활용
console.log(person1.name) // David
console.log(person1.age) // 35
person1.intro() // My name is David.

//---------------------------------------------------

// (상속을 사용할) 클래스 생성
class Child extends Person {
	constructor(name, age, mbti) {
		super(name, age)
		this.mbti = mbti
	}
  intro() {
    console.log(`Hi, I'm ${this.name}.`)
  }
  speakMBTI() {
    console.log(`My MBTI is ${this.mbti}!`)
  }
}

// 인스턴스 생성
const child1 = new Child('Jin', 10, 'INFJ')

// 인스턴스 활용
console.log(child1.name) // Jin
console.log(child1.age) // 10
child1.intro() // Hi, I'm Jin.
child1.speakMBTI() // My MBTI is INFJ!