TC = int(input())
for T in range(1, TC+1):
    N, he = input().split()
    de = int(he, 16)
    bi = format(de, 'b')
    if len(bi) < int(N)*4:
        bi = '0' + bi
    print(f'#{T} {bi}')
