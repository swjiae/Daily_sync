time = list(map(int, input().split()))

time.sort()

total = 0
for i in range(1, 4):
    total += time[i-1] * (4-i)

print(total)

# 첫번째 사용자는 대기 X - 제외
# 마지막 사용자 시간에 대기하는 사람 X - 제외
