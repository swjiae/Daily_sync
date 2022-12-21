TC = int(input())
numbers = [2, 3, 5, 7, 11]
for T in range(1, TC+1):
    exponent = []
    n = int(input())
    for i in range(len(numbers)):
        e = 0
        while n % numbers[i] == 0:
            n = n // numbers[i]
            e += 1
        exponent.append(e)
    print(f'#{T}', *exponent)
