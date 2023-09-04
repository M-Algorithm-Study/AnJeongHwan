import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
M, N, K = map(int, input().split())
# 1.몇 개의 분리된 영역 개수 2.각 영역의 넓이(오른차순 정렬) (N,M)

graph = [[0]*N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            graph[y][x] += 1

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
stack = []
count = 0
areas = []
# 모든 좌표를 순회하며 영역을 찾음
for x in range(N):
    for y in range(M):
        if graph[y][x] == 0:  # 아직 방문하지 않은 영역을 찾으면
            stack.append((x, y))  # 스택에 추가하고 방문 표시
            graph[y][x] = 1
            count += 1  # 영역 개수 증가
            temp_area = 0  # 현재 영역의 넓이를 저장할 변수 초기화
            while stack:
                x, y = stack.pop()  # 스택에서 좌표를 꺼내서
                temp_area += 1  # 영역의 넓이를 증가시키고
                for i in range(4):  # 상하좌우로 이동하며
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < N and 0 <= ny < M and graph[ny][nx] == 0:
                        graph[ny][nx] = 1  # 방문한 곳으로 표시하고
                        stack.append((nx, ny))  # 스택에 추가하여 연결된 영역을 탐색
            areas.append(temp_area)  # 현재 영역의 넓이를 리스트에 추가

# 영역의 개수 출력
print(count)

# 각 영역의 넓이를 오름차순으로 정렬하여 출력
areas.sort()
print(*areas)
