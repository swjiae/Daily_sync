arr = [list(input()) for _ in range(5)]
brr = ['M', 'A', 'P', 'O', 'M']
for i in range(5):
    arr[i][1], arr[i][3] = arr[i][3], arr[i][1]

flag = 0
for i in range(5):
    if arr[i] == brr:
        flag = 1

print('yes' if flag else 'no')

