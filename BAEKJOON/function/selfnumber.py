# 생성자가 없는 숫자

def Made(n):
    made = n
    while n != 0:
        made += n % 10
        n = n // 10
    return made

exception = []
for n in range(1, 10000):
    made = Made(n)
    exception.append(made)

for n in range(1, 10001):
    if n not in exception:
        print(n)