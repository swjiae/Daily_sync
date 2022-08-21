'''
3
3 10 5
1 3 5 7 9
3 10 5
1 3 7 8 9
5 20 5
4 7 9 14 17
'''
'''
#1 3
#2 0
#3 4
'''
TC = int(input())
for T in range(1, TC+1):
    K, N, M = map(int, input().split())
    arr_M = list(map(int, input().split()))
    bucket = [0] * 100
    for i in range(M):
        bucket[arr_M[i]] += 1
    now = 0 # idx
    cnt = 0
    flag = 0
    while 1:
        if now >= N:
            break
        move = 0
        for i in range(K, 0, -1):
            move += 1
            if bucket[now+i] == 1:
                now += i
                cnt += 1
                break
        if move >= K:
            flag = 1
            break
        if cnt > M:
            flag = 1
            break
    print(0) if flag else print(cnt)