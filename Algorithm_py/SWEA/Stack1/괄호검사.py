TC = int(input())
for T in range(1, TC+1):
    check = ['{', '}', '(', ')']
    a = list(input()) # print('{} {}'.format(1, 2))
    result = []
    while a:
        b = a.pop()
        if b in check:
            result.append(b)
        if len(result) >= 2:
            if result[-1] == '(' and result[-2] == ')' or result[-1] == '{' and result[-2] == '}':
                result.pop()
                result.pop()
    print(f'#{T}', 1 if len(result) == 0 else 0)