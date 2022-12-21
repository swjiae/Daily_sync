TC = int(input())
for T in range(1, TC+1):
    N = int(input())
    arr = list(map(int, input()))
    arr = sorted(arr, key=lambda x: (-arr.count(x), -x))
    num = arr[0]
    cnt = arr.count(num)
    print(f'#{T} {num} {cnt}')