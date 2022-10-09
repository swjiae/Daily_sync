'''
땅파기 문제
땅을 개척작업을 통해
가치를 올리고자 합니다.
(위아래좌우그리고 자기자신의 가치가 *7%10한 값으로 바뀜)

총 3곳을 개발할 예정..
중복가능( 한번 개발한 했던곳을 또 개발 가능)
개발후 3*3배열의 땅의가치가 Max가 되었을때
그 Max값을 출력해 주시면 됩니다.
'''

from copy import deepcopy

arr = [
    [4, 2, 1],
    [5, 3, 9],
    [7, 8, 1]
]

def digging(y, x):
    global arr
    dy = [0, -1, 1, 0, 0]
    dx = [0, 0, 0, -1, 1]
    for i in range(5):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < 3 and 0 <= nx < 3:
            arr[ny][nx] = arr[ny][nx]*7%10
    return

Max = 0
def dfs(level):
    global arr, Max
    backup = deepcopy(arr)
    if level == 3:
        sum = 0
        for i in range(3):
            for j in range(3):
                sum += arr[i][j]
        Max = max(sum, Max)
        return
    for y in range(3):
        for x in range(3):
            digging(y, x)
            dfs(level+1)
            arr = deepcopy(backup)
dfs(0)
print(Max)
