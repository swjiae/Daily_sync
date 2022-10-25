function palindrome(str) {
  const check = str.split('').reverse().join('')
  if (str === check) {
    console.log(true)
  } else {
    console.log(false)
  }
}

  // 출력
palindrome('level')
palindrome('hi')