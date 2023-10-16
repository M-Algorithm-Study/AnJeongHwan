import sys
sys.stdin = open("input.txt", "r")

N = int(input())

dp = [0] * (N + 1)

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1  # 1을 뺀 경우의 수(N-1의 최솟값 + 1)
    if i % 3 == 0:  # 3으로 나누어 떨어질 때
        dp[i] = min(dp[i], dp[i // 3] + 1)  # (N-1의 최솟값 + 1)과 3으로 나누었을 때 최솟값 비교
    if i % 2 == 0:  # 2로 나누어 떨어질 때
        # (N-1의 최솟값 + 1)과 3으로 나누었을 때 최솟값을 비교해서 나온 최솟값과 2로 나누었을 때 최솟값 비교
        dp[i] = min(dp[i], dp[i // 2] + 1)
print(dp[N])
