rate = ['A', 'B', 'C', 'D', 'E', 'F']
N, K = map(int, input().split())
result = [0]*(K+1)

# 등급
arr = [] # [['B', '4'], ['1', 'A'], ['3', 'B'], ['A', '1']]
# 그룹핑
brr = [] # [['3', '2'], ['3', '4']]

for _ in range(N):
    a, b = input().split()
    if a in rate or b in rate:
        arr.append([a, b])
    else:
        brr.append([a, b])

# 등급 입력하기
for i in range(len(arr)):
    a, b = sorted(arr[i])
    result[int(a)] = b # [0, 'A', 0, 'B', 'B']

# 그룹핑하기
for i in range(len(brr)):
    a, b = brr[i]
    a, b = int(a), int(b)
    if result[a] != 0:
        result[b] = result[a]
    if result[b] != 0:
        result[a] = result[b]
for i in range(1, K+1):
    print(result[i], end='')
