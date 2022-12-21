'''
TestCase
5
7
0 1 3
0 3 9
0 4 5
1 2 7
1 4 1
2 3 1
4 2 1
0
'''

# 입력받기
import heapq
N = int(input()) # 노드 개수
M = int(input()) # 간선 개수
arr = [[] for _ in range(N)]
for i in range(M):
    start, end, cost = map(int, input().split())
    arr[start].append([cost, end])
'''
A [[[3, 1], [9, 3], [5, 4]], 
B [[7, 2], [1, 4]], 
C [[1, 3]], 
D [], 
E [[1, 2]]]
'''
# 기본 setting
start = int(input())
inf = 21e8
result = [inf]*N # 최소 비용 update될 것임
heap = [] # 경유한 (비용, 도착) push될 예정

# 최소비용 구하는 함수
def dijkstra(start):
    result[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        s_v, v = heapq.heappop(heap)
        if result[v] < s_v:continue
        for i in arr[v]: # 경유지에서 갈 수 있는 [비용, 도착점]
            s_v_e = s_v + i[0]
            if s_v_e < result[i[1]]:
                result[i[1]] = s_v_e
                heapq.heappush(heap, (s_v_e, i[1]))

dijkstra(start)
print(*result)