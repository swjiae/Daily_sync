t = int(input())

for n in range(1, t+1):
    sum = 0
    for i in list(map(int, input().split())):
        if i % 2 != 0:
            sum = sum + i
    print(f'#{n} {sum}')


