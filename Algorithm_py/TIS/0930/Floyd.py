inf = 21e8
arr = [
    [0, 5, inf, 8],
    [7, 0, 9, inf],
    [2, inf, 0, 4],
    [inf, inf, 3, 0]
]

for i in range(4): # 경유지
    for j in range(4): # 시작점
        for k in range(4): # 도착점
            if arr[j][k] > arr[j][i] + arr[i][k]:
                arr[j][k] = arr[j][i] + arr[i][k]

print(arr)
'''
[[0, 5, 11, 8], 
[7, 0, 9, 13], 
[2, 7, 0, 4], 
[5, 10, 3, 0]]
'''