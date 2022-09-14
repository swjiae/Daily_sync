'''
1
5 1
2 1 2 5 1 6 5 3 6 4
'''
TC = int(input())
for T in range(1, TC+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    # 인접리스트 만들기
    tree = [[0] * 2 for _ in range(E + 2)]
    '''
      L  R
    [[0, 0], 부모
     [0, 0], # 1
     [0, 0], # 2
     [0, 0], # 3
     [0, 0], # 4
     [0, 0], # 5
     [0, 0]] # 6
    '''
    for i in range(len(arr)//2):
        p, c = arr[i*2], arr[i*2+1]
        if tree[p][0] == 0:
            tree[p][0] = c
        else:
            tree[p][1] = c
    '''
      L  R
    [[0, 0], 부모
     [6, 0], # 1
     [1, 5], # 2
     [0, 0], # 3
     [0, 0], # 4
     [3, 0], # 5
     [4, 0]] # 6
    '''
    # 이진트리 노드 카운트하는 함수 만들기
    cnt = 0
    def preorder(N):
        global cnt
        if N:
            cnt += 1
            preorder(tree[N][0]) # preorder(N*2)
            preorder(tree[N][1]) # preorder(N*2+1)

    # 결과 출력
    preorder(N)
    print(f'#{T} {cnt}')
