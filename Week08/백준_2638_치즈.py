import sys
from collections import deque
from pprint import pprint
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
time = 0

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)


def bfs():
    q = deque()
    visited = [[0] * m for _ in range(n)]

    q.append((0, 0))
    visited[0][0] = 1  # 0,0에 치즈가?

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 공기(0) 이고 방문 안했으면 다음 방문할 예정
                if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                elif graph[nx][ny] == 1:  # 치즈라면 방문 횟수 1 추가
                    visited[nx][ny] += 1

    melted = []  # 녹아야 될 치즈
    for i in range(n):
        for j in range(m):
            if visited[i][j] >= 2:  # bfs로 두 번 이상 방문한 치즈
                melted.append((i, j))

    return melted


while True:
    melted = bfs()

    if not melted:  # 더 이상 녹을 치즈 없으면 멈춤
        break

    time += 1  # 녹아 없어지는데 걸리는 시간 추가

    for x, y in melted:  # 치즈 녹이고 공기로 바꾸기
        graph[x][y] = 0

print(time)


# import sys
# from pprint import pprint
# sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline
# n, m = map(int, input().split())
# graph = []
# time = 0

# for i in range(n):
#     temp = list(map(int, input().split()))
#     graph.append(temp)

# pprint(graph)

# # 2변 이상 공기와 접촉하는 치즈 찾기
# # 치즈 내부에 있는 공간은 제외 하기

# # 1. 내부에 있는 공기(?) 숫자 2로 바꾸기//상하좌우에 1이 있는지 확인
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 0:
#             check = 0
#             for a in range(i, n):  # 오른쪽 확인
#                 if graph[a][j] == 1:
#                     check += 1
#                     break
#             for b in range(i, -1, -1):  # 왼쪽 확인
#                 if graph[b][j] == 1:
#                     check += 1
#                     break
#             for c in range(j, m):  # 아래 확인
#                 if graph[i][c] == 1:
#                     check += 1
#                     break
#             for d in range(j, -1, -1):  # 위 확인
#                 if graph[i][d] == 1:
#                     check += 1
#                     break
#             if check == 4:
#                 graph[i][j] = 2
# pprint(graph)

# # 2. 전체를 탐색해서 0을 2개 이상 접하고 있는 1을 찾기


# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 1:
#             air = 0
#             for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#                 nx, ny = i + dx, j + dy
#                 if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
#                     air += 1
#             if air >= 2:
#                 graph[i][j] = z
