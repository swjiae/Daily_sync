'''
잘려진 쇠막대기 조각의 총 개수
2
()(((()())(())()))(())
(((()(()()))(())()))(()())
'''
TC = int(input())
for T in range(1, TC+1):
    a = input()
    stack = []
    cnt = 0
    for i in range(len(a)):
        if a[i] == '(':
            stack.append('(')
        else:
            # 레이저 일 때
            if a[i-1] == '(':
                stack.pop()
                cnt += len(stack)
            # 레이저 아닐 때
            else:
                stack.pop()
                cnt += 1
    print(f'#{T} {cnt}')