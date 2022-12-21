/* 
  1. 아래 코드를 object destructuring을 활용해 리팩토링 하시오.
  2. Rest operator를 활용해 아래 코드를 리팩토링 하시오.
  3. Spread operator를 활용해 아래 코드를 리팩토링 하시오.
*/

// 1-1
const savedFile = {
    name: 'profile',
    extension: 'jpg',
    size: 29930
  }

const { name, extension } = savedFile
console.log(`The file ${name}.${extension} is size of ${size} bytes.`)


// 1-2
const data = {
  username: 'myName',
  password: 'myPassword',
  email: 'my@mail.com',
}

const { username, password, email } = data



// 2
function addNumbers(...theArgs) {
  const numbers = [...theArgs]
  return numbers.reduce((sum, number) => { 
    return sum += parseInt(number)
  }, 0)
}
console.log(addNumbers(1, 2, 3, 4, 5))

// 3-1
const defaultColors = ['red', 'green', 'blue'];
const palette = ['navy', 'black', 'gold', 'white', ...defaultColors]
console.log(palette)

// 3-2
const info1 = { name: 'Tom', age: 30 }
const fullInfo = { ...info1, isMarried: true, balance: 3000 }
console.log(fullInfo)