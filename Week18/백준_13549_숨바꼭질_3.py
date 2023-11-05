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
        
        next = [2*cur, cur-1, cur+1]

        for i in next:
            if 0 <= i < 100001 and visited[i] == -1: # i가 범위 안에 있고 방문하지 않았다면

                if i == 2*cur:
                    visited[i] =  visited[cur]  # 2배한 경우에는 0초 소요
                    q.appendleft(i) # 방문 순서상 먼저 방문하도록

                else:
                    visited[i] = visited[cur] + 1 # 1초 소요
                    q.append(i)

bfs(N)