'''
1
2
1 3
2 5
5
1
2
3
4
5
'''
'''
#1 1 2 2 1 1
'''
TC = int(input())
for T in range(1, TC+1):
    N = int(input())
    Range = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    stop = list(int(input()) for _ in range(P))
    bucket = [0]*5001
    for i in range(N):
        A, B = Range[i][0], Range[i][1]
        for i in range(A, B+1):
            bucket[i] += 1

    result = []
    for i in stop:
        result.append(bucket[i])

    print(f'#{T}', *result)