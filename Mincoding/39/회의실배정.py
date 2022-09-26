N = int(input())
book = []
for i in range(N):
    book.append(list(map(int, input().split())))

book.sort(key=lambda x:x[1])

b_time = -1
cnt = 0
for i in range(N):
    if b_time <= book[i][0]:
        b_time = book[i][1]
        cnt += 1

print(cnt)