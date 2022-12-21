// 1. Promise 사용해보기 (hi -> ssafy -> bye 출력되도록)
// promise 객체를 반환하는 함수 선언

function printSSAFY() {
    return new Promise(function (resolve, reject) {
        setTimeout(() => {
            console.log('SSAFY')
            resolve()
        }, 3000)
    })
}

console.log('Hi')
printSSAFY().then(() => {
    console.log('Bye')
})

// 2. Promise 조금 더 뜯어보기 - Promise의 3가지 상태
// 2.1 Pending(대기) 상태
