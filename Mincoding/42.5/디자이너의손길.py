from copy import deepcopy

# 입력받기
st = input()
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
path = []
used = [0]*len(st)
Max = 0
def dfs(level):
    global Max
    if level == len(st):
        tmp = deepcopy(path)
        total = getscore(tmp)
        Max = max(total, Max)
        return
    for i in range(len(st)):
        if used[i] == 1: continue
        used[i] = 1
        path.append(st[i])
        dfs(level+1)
        path.pop()
        used[i] = 0
dfs(0)

# 출력하기
print(Max)