TC = int(input())
for T in range(1, TC+1):
    Max = 0
    a = input()
    b = input()
    for i in a:
        tmp = b.count(i)
        Max = max(Max, tmp)
    print(f'#{T} {Max}')
