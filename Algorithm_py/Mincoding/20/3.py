arr = list(map(int, input().split()))

def recur(level):
    print(arr[level])
    if level == len(arr)-1:
        return
    recur(level+1)
    print(arr[level])

recur(0)