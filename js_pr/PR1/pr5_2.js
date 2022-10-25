const participantNums =  [[1, 3, 2, 2, 1], 
[3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21],
[9, 1, 8, 7, 71, 33, 62, 35, 11, 4, 7, 71, 33, 8, 9, 1, 4, 11, 35]
]

participantNums.forEach((tc) => {
	let maxValue = Math.max(...tc)
	let bucket = new Array(maxValue).fill(0)
    
    tc.forEach((value) => {
        bucket[value] += 1
    })

    for (let i = 0; i < bucket.length; i++) {
        if (bucket[i] === 1) {
            console.log(i)
        }
    }
})
