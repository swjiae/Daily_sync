a, b = map(int, input().split())

def recur(a):
    global b
    if a == b:
        print(a)
        return
    print(a)
    recur(a+1)
    print(a)

recur(a)