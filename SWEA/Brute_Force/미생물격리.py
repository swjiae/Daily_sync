# M시간 후 남아 있는 미생물 수의 총합
# 약품에 닿으면, (1) 미생물 수 : 미생물 수//2  (2) 방향 : 반대
# 군집이 만나면, (1) 미생물 수 : 군집합  (2) 방향 : 가장 미생물이 많은 군집

# 입력받기
N, M, K = map(int, input().split()) # N:셀의개수 M:격리시간 K:미생물군집의개수
arr = [[]*N for _ in range(N)]

for _ in range(K):
    y, x, k, d = map(int, input().split())
    print(k, d)
    arr[y][x].append(k)
    arr[y][x].append(d)
print(arr)

'''
7 2 9
1 1 7 1
2 1 7 1
5 1 5 4
3 2 8 4
4 3 14 1
3 4 3 3
1 5 8 2
3 5 100 1
5 5 1 1
'''
