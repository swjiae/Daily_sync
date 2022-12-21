TC = int(input())
for T in range(1, TC+1):
    A, B = list(input().split())

    def pattern(i):
        for j in range(len(B)):
            if A[i+j] != B[j]:
                return 0
            return 1

    cnt = 0
    for i in range(len(A) - len(B) + 1):
        cnt += pattern(i)
    result = len(A) - (len(B)-1) * cnt
    print(f'#{T} {result}')
