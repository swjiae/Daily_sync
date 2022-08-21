# a for문 b for문 swap if문을
# while로 감싸는..?
arr = list(map(int, input().split()))
pivot = 0 # pivot index
a = 1 # pivot 다음 index
b = 7 # 마지막 index

while 1:
    # arr[a] : pivot 보다 큰 값 찾기
    for i in range(8-a):
        if arr[a] < arr[pivot]:
            a += 1
        elif arr[a] > arr[pivot]:
            break
    # arr[b] : pivot 보다 작은 값 찾기
    for i in range(0+b):
        if arr[b] > arr[pivot]:
            b -= 1
        elif arr[b] < arr[pivot]:
            break
    # 만약 a 보다 b가 작아지면 b랑 pivot 자리 바꾸고 while문 끝내기
    if a > b:
        arr[pivot], arr[b] = arr[b], arr[pivot]
        break
    # swap
    arr[a], arr[b] = arr[b], arr[a]

print(*arr)