N = int(input())
arr = [list(input()) for _ in range(N)]

def row(st, ed):
    while 1:
        mid = (st+ed)//2
        if st > ed:
            return st-1
        if arr[mid][0] == '#':
            st = mid + 1
        elif arr[mid][0] == '0':
            ed = mid - 1

def column(st, ed, y):
    while 1:
        mid = (st+ed)//2
        if st > ed:
            return st-1
        if arr[y][mid] == '#':
            st = mid + 1
        elif arr[y][mid] == '0':
            ed = mid - 1

st, ed = 0, N-1
y = row(st, ed)
x = column(st, ed, y)

print(y, x)