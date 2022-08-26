arr = ['ABCD', 'ABCE', 'AGEH', 'EIEI', 'FEQE', 'ABAD']
word = input()

idx = []
for i in range(4):
    if word[i] != '?':
        idx.append(i)

cnt = 0
for i in range(6):
    flag = 1
    for x in range(idx):
        if arr[i][x] != word[x]:
            flag = 0
    if flag:
        cnt += 1
