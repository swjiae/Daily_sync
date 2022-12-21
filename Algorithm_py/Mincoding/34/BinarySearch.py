arr = [4, 4, 5, 7, 8, 10, 20, 22, 23, 24]
bst = [0]*1000

# bst 입력받기
def insert(value):
    now = 1
    while 1:
        if bst[now] == 0:
            bst[now] = value
            return
        if bst[now] < value: # value가 더 크면
            now = now*2+1 # 오른쪽에 insert
        else: # value가 더 작으면
            now = now*2 # 왼쪽에 insert

# target 찾기
def search(target):
    now = 1
    while 1:
        if now >= 1000: # 배열 범위보다 커지면
            return 0
        if bst[now] == 0: # target이 없으면
            return 0
        if bst[now] == target: # target을 찾았으면
            return 1
        if bst[now] < target: # target이 더 크면
            now = now*2+1 # 오른쪽 search
        else: # target이 더 작으면
            now = now*2 # 왼쪽 search

for i in range(len(arr)):
    insert(arr[i])
target = int(input())
result = search(target)
print('O' if result else 'X')