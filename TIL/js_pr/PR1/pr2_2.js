// function palindrome(str) {
//   // 문자열은 reverse() 함수가 없다
//   // 문자열 -> 배열 -> reverse -> 문자열
//   const reversed = str.split('').reverse().join('')
//   return reversed === str ? true : false
// }
  
// // 출력
// console.log(palindrome('level'))
// console.log(palindrome('hi'))

// ---------every 사용--------------------------------------------

function palindrome(str) {
  return str.split('').every((element, idx) => 
    element === str[str.length - 1 - idx]
  )
}
console.log(palindrome('level'))
console.log(palindrome('hi'))