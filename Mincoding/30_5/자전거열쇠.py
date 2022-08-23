# level = 4
# brunch = 26
arr = [chr(i) for i in range(65, 91)]
n = int(input())
password = [input() for _ in range(n)]
path = [''] * 4
cnt = 0
def abc(level):
    global cnt
    if level == 4:
        cnt += 1
        for i in password:
            if i == ''.join(path):
                print(cnt)
        return
    for i in range(26):
        path[level] = arr[i]
        abc(level+1)

abc(0)