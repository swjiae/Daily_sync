'''
[7 3 5 4]
각각의 숫자에
2를 곱하거나 또는
3으로 나누거나 또는
5를 더해서 숫자를 바꾼 후

바뀐 4개의 숫자들의 곱을 구한 후
그 곱의 Max값을 출력해 주세요.

(추가설명)
7 3 5 4 가 있다면
7에 2를 곱하거나 3으로 나누거나 5을 더한 값으로 바꿈
3에 2를 곱하거나 3으로 나누거나 5을 더한 값으로 바꿈
5에 2를 곱하거나 3으로 나누거나 5을 더한 값으로 바꿈
4에 2를 곱하거나 3으로 나누거나 5을 더한 값으로 바꿈

바뀐 숫자들을 모두 곱했을때 MAX 값 출력하기
'''

arr = [7, 3, 5, 4]
Max = 0
def dfs(level, multi):
    global Max
    if level == 4:
        Max = max(Max, multi)
        return
    dfs(level+1, multi*(arr[level]*2))
    dfs(level+1, multi*(arr[level]//3))
    dfs(level+1, multi*(arr[level]+5))

dfs(0, 1)
print(Max)