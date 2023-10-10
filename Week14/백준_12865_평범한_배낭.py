import sys
input = sys.stdin.readline

# N개의 물건, 무게 W, 가치 V
# 최대 K만큼의 무게
# 물건들의 가치v 합의 최댓값

n, k = map(int, sys.stdin.readline().split())  # 물품의 수, 버틸 수 있는 무게
arr = [(0, 0)]  # 무게 w, 가치 v 넣을 리스트
chart = [[0] * (k + 1) for _ in range(n + 1)]
for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    arr.append((w, v))

for i in range(1, n + 1):   # 물건 하나씩(arr에서 (i,j))
    for j in range(1, k + 1):  # 1~k무게까지 표 작성
        w = arr[i][0]
        v = arr[i][1]
        if j < w:   # 해당 물건이 더 큰 경우, 이전 값으로 넣기(가방에 해당 물건을 넣을 수 없을 때)
            chart[i][j] = chart[i - 1][j]
        else:   # 해당 물건이 들어가는 사이즈인 경우
            chart[i][j] = max(v + chart[i - 1][j - w], chart[i - 1][j])
            # dp[i][j] = max(현재 물건 가치 + dp[이전 물건][현재 가방 무게 - 현재 물건 무게], dp[이전 물건][현재 가방 무게])
            # dp[i][j] = max(현재 물건 가치 + dp[이전 물건까지의 가방무게][현재 가방에 들어있는 무게 - 현재 물건 무게], dp[이전 물건][현재 가방 무게])
            # 이전 값과 비교

print(chart[n][k])
