// map : 배열의 각 요소에 함수 적용 + return

// filter : map + 조건이 true인 값 return

// find : map + 조건의 첫번째 true 값만 return (없으면 -1 return)

// every : map + 조건이 모두 참일 때 true return (하나라도 false면 false return)

// some : map + 조건이 하나라도 참일 때 true return (모두 false면 false return)

// reduce : 배열의 각 요소에 함수 적용하여 누적합 및 평균 구할 때 사용

const nums = [1, 2, 3, 4]

const result = nums.map((num) => num**3)

console.log(result)