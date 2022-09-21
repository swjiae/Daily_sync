TC = int(input())
for T in range(1, TC+1):
    de = float(input()) # 0.165
    cnt = 0
    bi = '' # 2진수 출력할 값
    while de > 0 and cnt < 13:
        temp = de * 2
        bi += str(temp)[0]
        de = temp - int(temp)
        cnt += 1
    if cnt == 13:
        print(f'#{T} overflow')
    else:
        print(f'#{T} {bi}')
