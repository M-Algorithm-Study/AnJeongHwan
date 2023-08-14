from collections import deque
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())

graph = []

for _ in range(N):
    graph.append(list(map(int, input())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, x, y):

    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    count = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                count += 1

    return count


result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            count = bfs(graph, i, j)  # BFS로 연결된 집 개수를 계산
            result.append(count)  # 연결된 집 개수를 결과 리스트에 추가

result.sort()  # 결과 리스트를 오름차순으로 정렬

print(len(result))  # 총 단지 수를 출력
for i in result:
    print(i)  # 각 단지별 집 개수를 출력
