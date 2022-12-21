TC = int(input())
for T in range(1, TC+1):
    N = int(input())

    stop = [0] * 1001 # 1~1000번 정류쟝
    for _ in range(N):
        bus, A, B = map(int, input().split())
        if bus == 1: # 일반버스
            for i in range(A, B+1):
                stop[i] += 1
        elif bus == 2: # 급행
            if A%2 == 0:
                for i in range(A+1, B):
                    if i%2 == 0:
                        stop[i] += 1
            else:
                for i in range(A+1, B):
                    if i%2 == 1:
                        stop[i] += 1