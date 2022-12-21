'''
3
10 5 2 + 3 4 + * .
5 3 * + .
1 5 8 10 3 4 + + 3 + * 2 + + + .
'''
TC = int(input())
for T in range(1, TC+1):
    arr = list(input().split())
    stack = []
    while arr[0] != '.':
        now = arr.pop(0)
        if now.isdigit():
            stack.append(int(now))
        else:
            if len(stack) >= 2:
                a = stack.pop()
                b = stack.pop()
                if now == '+':
                    result = b + a
                    stack.append(result)
                elif now == '-':
                    result = b - a
                    stack.append(result)
                elif now == '/':
                    result = b // a
                    stack.append(result)
                else:
                    result = b * a
                    stack.append(result)
            else:
                stack = ['error']
                break
    if len(stack) != 1:
        stack = ['error']
    print(f'#{T} {stack[0]}')