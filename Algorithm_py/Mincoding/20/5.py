arr = list(input())
path = []

def recur(level):
    if level == len(arr):
        return
    # print(arr[level])
    recur(level+1)
    print(arr[level])

recur(0)
