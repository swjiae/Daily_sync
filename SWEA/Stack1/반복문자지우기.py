TC = int(input())
for T in range(1, TC+1):
    a = list(input())
    result = []
    while a:
        result.append(a.pop())
        if len(result) >= 2:
            if result[-1] == result[-2]:
                result.pop()
                result.pop()

    print(f'#{T} {len(result)}')


