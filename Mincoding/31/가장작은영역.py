n = int(input())
arr = list(map(int, input().split()))
k = 4

def SW(arr, k):
    start = 0
    Sum = 0
    Min = 21e8
    for end in range(n):
        Sum += arr[end]
        if end >= k-1:
            if Sum < Min:
                Min = Sum
            Sum -= arr[start]
            start += 1
    print(Min)

SW(arr, k)