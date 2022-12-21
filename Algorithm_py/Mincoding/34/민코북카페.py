N = int(input())
books = list(input().split())
books.sort()
M = int(input())
for i in range(M):
    book, time = input().split()
    time = int(time)
    st = 0
    ed = len(books)-1
    flag = 0
    while time:
        mid = (st+ed)//2
        if books[mid] == book:
            flag = 1
            break
        if books[mid] < book:
            st = mid + 1
        else:
            ed = mid - 1
        time -= 1
    print('pass' if flag else 'fail')