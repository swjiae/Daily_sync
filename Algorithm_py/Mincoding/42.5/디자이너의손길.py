from copy import deepcopy

# 입력받기
st = list(input())
N = int(input())

# 점수 계산하는 함수
def getscore(path): # ['A', 'A', 'C', 'H', 'Z']
    total = 0
    for i in range(len(path)-1):
        score = abs(ord(path[i]) - ord(path[i+1]))
        if score == 0:
            total -= 50
        elif score <= 5:
            total += 3
        elif score >= 20:
            total += 10
    return total

# swap 한 경우의 수 뽑으면서 총점수 계산하기
used = [0]*len(st)
Max = 0
def dfs(level, start):
    global Max, st
    if level == N:
        total = getscore(st)
        Max = max(total, Max)
        return
    for i in range(start, len(st)-1):
        for j in range(i+1, len(st)):
            backup = deepcopy(st)
            st[i], st[j] = st[j], st[i]
            dfs(level+1, i+1)
            st = deepcopy(backup)
dfs(0, 0)

# 출력하기
print(Max)