'''
line1=[3,7,1,-3,-6,1]
line2=[7,-4,1,-5,3,2]

두 라인에서 숫자를 1개씩 번갈아 가며 선택을
하고자 합니다.
첫번째 라인에서 숫자를 1개 택한 후 *1을 하고
두번째 라인에서 숫자를 1개 택한 후 *2를 하고
첫번쨰 라인에서 숫자를 1개 택한 후 *3을 하고..
두번째 라인에서 숫자를 1개 택한 수 *4를 하는등
가중치가 1씩 증가되는 값으로 뽑은 숫자에 곱해 줍니다.

가중치를 곱한 후 모두 더했을때
합이 0에 가장 가까운 수를 구하고자 합니다.
이때 총 합은 몇일까요?
(각 라인의 숫자는 1번씩만 사용하여 모든 숫자를 한번씩 뽑습니다.)
'''

line1 = [3, 7, 1, -3, -6, 1]
line2 = [7, -4, 1, -5, 3, 2]
used1 = [0]*6
used2 = [0]*6
Min = 21e8
def dfs(level, sum):
    global Min
    if level == 12:
        gap = abs(0 - sum)
        Min = min(Min, gap)
        return
    if level % 2 == 0:
        for i in range(6):
            if used1[i] == 1: continue
            used1[i] = 1
            dfs(level+1, sum+(line1[i]*(level+1)))
            used1[i] = 0
    else:
        for i in range(6):
            if used2[i] == 1: continue
            used2[i] = 1
            dfs(level+1, sum+(line2[i]*(level+1)))
            used2[i] = 0

dfs(0, 0)
print(Min)