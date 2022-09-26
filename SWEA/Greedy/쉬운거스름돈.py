TC = int(input())
for T in range(1, TC+1):
    won = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    change = int(input())

    total = []
    for i in range(len(won)):
        cnt = change // won[i]
        total.append(cnt)
        change -= cnt * won[i]

    print(f'#{T}')
    print(*total)