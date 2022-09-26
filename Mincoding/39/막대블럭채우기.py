N = int(input())

length = list(map(int, input().split()))

length.sort()

total = 100
cnt = 0
for i in range(N):
    total -= length[i]
    if total < 0:
        break
    cnt += 1

print(cnt)