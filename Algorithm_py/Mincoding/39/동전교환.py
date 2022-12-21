coin = [500, 100, 50, 10]
change = int(input())

total = 0
for i in range(len(coin)):
    cnt = change // coin[i]
    total += cnt
    change -= cnt * coin[i]

print(total)