# 상근이 카드
N = int(input())
nrr = list(map(int, input().split()))
nrr.sort()

# 확인할 카드
M = int(input())
mrr = list(map(int, input().split()))

# Binary Search
def BS(target):
    st, ed = 0, N - 1
    while 1:
        mid = (st + ed) // 2
        if nrr[mid] == target:
            return 1
        elif nrr[mid] > target:
            ed = mid - 1
        elif nrr[mid] < target:
            st = mid + 1
        if st > ed:
            return 0

# target
result = []
for i in range(M):
    target = mrr[i]
    ret = BS(target)
    result.append(ret)

print(*result)