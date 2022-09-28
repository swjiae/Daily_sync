N = int(input())
result = []
for i in range(N+1):
    if i < 2:
        result.append(1)
    else:
        result.append(result[i-2] + result[i-1])

print(result[-1])
