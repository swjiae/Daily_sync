N = int(input())
requests = list(map(int, input().split()))
budget = int(input())

if sum(requests) <= budget:
    print(max(requests))
else:
    requests.sort()
    cha = sum(requests) - budget
    idx = N-1
    gop = 1
    while 1:
        if idx == 0:
            print(budget // N)
            break
        cal = (requests[idx] - requests[idx-1]) * gop
        if cal > cha:
            print(requests[idx-1] + (cal-cha)//gop)
            break
        else:
            cha -= (requests[idx] - requests[idx-1]) * gop
            idx -= 1
            gop += 1