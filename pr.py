ar=[
    [11,14],
    [18,22],
    [15,17],
    [10,12],
    [18,21],
    [10,13],
    [12,14],
    [16,18],
    [12,15],
    [17,19],
    [14,15],
    [11,15],
    [19,22],
    [19,20],
    [21,22],
    [18,22]
]
ar.sort()
result = []
Min = 21e8
used = [0]*(len(ar)+1)
for _ in range(len(ar)-1):
    for i in range(len(ar)-1):
        if ar[i][1] < ar[i+1][0]:
            tmp = abs(ar[i][0] - ar[i][1])
            Min = min(Min, tmp)
    result.append(Min)

print(len(result))