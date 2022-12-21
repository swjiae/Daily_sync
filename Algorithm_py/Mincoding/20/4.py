n = int(input())

def recur(level, n):
    if level == 3:
        print(n)
        return
    recur(level+1, n+2)
    print(n)

recur(0, n)