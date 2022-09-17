arr = [15, 20, 44, 22, 55, 16, 45]
first = list(input())
Del = int(input())
N = len(first)-Del
Max = 0
def buy(level, start, sum):
    global Max
    if level == N:
        if sum % 10 == 0:
            Max = max(sum, Max)
        return
    for i in range(start, len(first)):
        Add = arr[ord(first[i]) - 97]
        buy(level+1, i+1, sum+Add)

buy(0, 0, 0)
print(Max)