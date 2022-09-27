TC = int(input())
for T in range(1, TC+1):
    N, M = map(int, input().split()) # 배열크기, 회문크기
    arr = [list(input()) for _ in range(N)]
