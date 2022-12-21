n = int(input())
Max = 50
Min = 1
flag = 1
for _ in range(n):
    a, b = input().split()
    a = int(a)
    if Max < a or Min > a:
        print('ERROR')
        flag = 0
        break
    if b == 'DOWN':
        Max = a - 1
    if b == 'UP':
        Min = a + 1
    if Max - Min == 1:
        print(Min)
        flag = 0
        break

if flag:
    print(f'{Min} ~ {Max}')




