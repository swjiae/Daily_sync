# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.\
# 각 테스트 케이스에는 N이 주어지고 다음 줄부터 N+1줄까지 Ci와 Ki가 빈 칸을 사이에 두고 주어진다.
# 1
# 3
# A 10
# B 7
# C 5 

# [출력]
# 각 줄은 '#t'로 시작하고, 다음 줄부터 원본 문서를 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
# #1
# AAAAAAAAAA
# BBBBBBBCCC
# CC

T = int(input())
for t in range(1, T+1):
    N = int(input())
    result = ""
    for i in range(N):
        ci, ki = input().split()
        ki = int(ki)
        result = result + ci * ki

    print("#{}".format(t))
    for i in range(len(result)):
        if (i+1) % 10 == 0:
            print(result[i])
        else:
            print(result[i], end="")
    print()

# txt = "My name is {}, I'm {}".format("John",36)
# a, b, c = input().split() or a = list(input().split())