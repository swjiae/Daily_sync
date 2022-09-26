n=int(input())
time_w=list(map(int,input().split()))

time_w.sort(reverse=True)

print(time_w)

answer=0
for i in range(1, n+1):
    answer += (i*time_w[i-1])

print(answer)