import sys
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1] * N  # N의 범위 만큼 dp 리스트

for i in range(N):
    max_dp = 1
    for j in range(i):
        if A[j] < A[i] and max_dp <= dp[j]:  # 증가 수열이면서 dp최댓값보다 크면 갱신
            max_dp = dp[j] + 1
    dp[i] = max_dp  # 기존 dp 최댓값 + 1

print(max(dp))
