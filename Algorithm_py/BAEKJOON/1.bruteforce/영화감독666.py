n = int(input())
num = 666
cnt = 1
while 1:
    if cnt == n:
        break
    num += 1
    if '666' in str(num):
        cnt += 1

print(num)