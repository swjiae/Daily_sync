P = int(input()) # 숫자반죽
N = int(input()) # 반복횟수

for _ in range(N):
    P = P * 2
    P = str(P)
    P = P[::-1] # int는 안되고 string은 됨
    P = int(P)

print(P)