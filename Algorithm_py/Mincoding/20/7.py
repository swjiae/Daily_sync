idx = int(input())
arr = [3, 7, 4, 1, 9, 4, 6, 2]

def recur(idx):
    if idx == 0:
        print(arr[idx])
        return
    print(arr[idx])
    recur(idx-1)
    print(arr[idx])

recur(idx)