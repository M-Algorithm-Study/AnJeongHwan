from collections import deque
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, k = map(int, input().split())  # n 수빈 k 동생 위치


# 방문한 위치를 기록
visited = [False] * 100001


def bfs(start, target):
    queue = deque([(start, 0)])  # 위치와 이동 횟수를 함께 큐에 저장
    visited[start] = True

    while queue:
        position, steps = queue.popleft()

        if position == target:
            return steps

        # 가능한 다음 위치들을 생성
        next_positions = [position - 1, position + 1, position * 2]

        for next_pos in next_positions:
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, steps + 1))


result = bfs(n, k)
print(result)

# import sys
# sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline
# n, k = map(int, input().split())  # n 수빈 k 동생 위치
# distance = k-n
# if distance == 0:
#     print(0)
#     exit()
# elif distance < 0:
#     n, k = k, n
# else:
#     pass

# cnt = 0
# while True:
#     a = abs(k-(2*n))
#     b = abs(k-(n+1))
#     c = abs(k-(n-1))
#     cnt += 1
#     if a <= b and a <= c:
#         n = 2 * n
#     elif b <= a and b <= c:
#         n += 1
#     else:
#         n -= 1
#     if abs(n - k) == 0:
#         break


# print(cnt-1)
