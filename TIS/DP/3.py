arr = [
    [0, 1, 1, 9],
    [4, 2, 2, 3],
    [1, 3, 4, 1],
    [3, 7, 8, 0]
]

for i in range(3):
    arr[0][i+1] += arr[0][i]
    arr[i+1][0] += arr[i][0]

'''
[[0, 1, 2, 11], 
 [4, 2, 2, 3], 
 [5, 3, 4, 1], 
 [8, 7, 8, 0]]
'''

for i in range(1, 4):
    for j in range(1, 4):
        arr[i][j] += min(arr[i-1][j], arr[i][j-1])

print(arr[3][3])