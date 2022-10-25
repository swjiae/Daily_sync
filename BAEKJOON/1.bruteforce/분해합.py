N = int(input())
Min = 21e8
for M in range(1, N):
    K = M
    nums = list(str(M))
    for i in range(len(nums)):
        K += int(nums[i])
    if K == N:
        Min = min(M, Min)
print(0 if Min == 21e8 else Min)