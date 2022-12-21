arr = ['_'] * 5
idx, life = map(int, input().split())
for i in range(life+1):
    arr[idx+i-1] = '_'
    arr[idx+i] = life-i
    if idx+i == 4:
        arr[idx+i] = '_'
    print(*arr, sep='')

