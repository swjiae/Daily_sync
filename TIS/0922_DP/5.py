change = 14
coin = [1, 7, 10]

arr = [[0 for _ in range(15)] for _ in range(3)]
for i in range(3):
    for j in range(15):
        mok = j // coin[i]
        if j % coin[i] == 0:
            arr[i][j] = mok
        else:
            if mok == 0:
                arr[i][j] = arr[i-1][j]
            else:
                arr[i][j] = min(arr[i-1][j], mok+arr[i][j%coin[i]])

print(arr[2][14])
