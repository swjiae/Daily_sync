const participantNums =  [[1, 3, 2, 2, 1], 
[3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21],
[9, 1, 8, 7, 71, 33, 62, 35, 11, 4, 7, 71, 33, 8, 9, 1, 4, 11, 35]
]

for (let i = 0; i < participantNums.length; i++) {
  const bucket = []

  for (let b = 0; b < 1000; b++) {
    bucket.push(0)
  }

  let result = participantNums[i].forEach((idx) => {
    bucket[idx] += 1
  })
  
  for (let j = 0; j < 1000; j++) {
    if (bucket[j] === 1) {
      console.log(j)
    }
  }
}

// 3
// 100
// 62