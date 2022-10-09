n = int(input())

def recur(level):
    print(level)
    if level == 0:
        return
    recur(level-1)
    print(level)

recur(n)