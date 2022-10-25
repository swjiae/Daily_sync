// 1번
const nums = [1,2,3,4,5,6,7,8]

for (let i = 0; i < nums.length; i++) {
  console.log()
}
// for (const i = 0; i < nums.length; i++) {
//                                     ^
// TypeError: Assignment to constant variable.

// for 문을 돌릴 때, 변수 i가 다른 값으로 할당 되어야 하기 때문에
// const i = 0 을 let i = 0 로 바꿔준다.

//-------------------------------------------------------

// 2번
for (num of nums) {
  console.log(num, typeof num)
}

// for ... in 을 사용하면 array의 key를 반환하기 때문에 type이 string이다.
// for ... of 로 수정하여 array의 value를 반환하면 type으로 number가 출력된다.
