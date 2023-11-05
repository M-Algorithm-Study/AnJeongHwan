from collections import deque
N, K = map(int, input().split())

visited = [-1]*100001

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 0

    while q:
        
        cur = q.popleft()

        if cur == K:
            print(visited[cur])
            return
        
        next = [2*cur, cur+1, cur-1]

        for i in next:
            if 0 <= i < 100001 and (visited[i] == -1 or visited[i] > visited[cur]):
            # i가 범위 안에 있고 방문하지 않았거나 기존 방문보다 더 빠르게 방문한 경우 (4>6 가는 경우: cur+1, cur-1일 때와  cur-1, cur+1 일 때 결과가 달라짐. 4 5 6 과 4 3 6 시간 차이)

                if i == 2*cur:
                    visited[i] =  visited[cur]  # 2배한 경우에는 0초 소요
                    q.appendleft(i) # 방문 순서상 먼저 방문하도록

                else:
                    visited[i] = visited[cur] + 1 # 1초 소요
                    q.append(i)

bfs(N)