'''
8
1 W 2 3
2 F 4 5
3 R 6 7
4 O 8
5 T
6 A
7 E
8 S
'''
TC = int(input())
for T in range(1, TC+1):
    N = int(input())
    arr = [i for i in range(0, N+1)]
    word = [''] * (N+1)
    for i in range(1, N+1):
        tmp = list(input().split())
        word[i] = tmp[1]

    def inorder(now):
        if now > N:
            return
        inorder(now*2)
        print(word[now], end='')
        inorder(now*2+1)

    print(f'#{T}', end=' ')
    inorder(1)
