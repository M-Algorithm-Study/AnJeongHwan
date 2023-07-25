# 계단 오르기
import sys

input = sys.stdin.readline

N = int(input())
stair = [int(input()) for i in range(N)]
dp = [0] * (N)

if len(stair) <= 2:
    print(sum(stair))
else:  # 계단이 4개 이상일 때
    dp[0] = stair[0]  # 첫번째 계단(첫번째 밟는 경우)
    dp[1] = stair[0] + stair[1]  # 두번째 계단(무조건 첫번째랑 두번째 계단 밟는 경우 최대)
    dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])  # 세번째 계단()

    for i in range(3, N):  # 네번째 계단 부터 dp 최대값 구하기
        dp[i] = max(dp[i - 3] + stair[i - 1] + stair[i], dp[i - 2] + stair[i])
        # i번째 계단을 오를 때
        # 전(n-1)계단과 전전전(n-3)계단을 밟고 오른 경우 vs 전전(n-2)계단을 밟고 오른 경우
    print(dp[N - 1])


# N = int(input())
# stair = [int(input()) for i in range(N)]
# dp = [0] * (N)
# if len(stair) <= 2:
#     print(sum(stair))
# else:  # 계단이 3개 이상일 때
#     dp[0] = stair[0]  # 첫째 계단
#     dp[1] = stair[0] + stair[1]  # 둘째 계단까지
#     for i in range(2, N):  # 3번째 계단 부터 dp 최대값 구하기
#         dp[i] = max(dp[i - 3] + stair[i - 1] + stair[i], dp[i - 2] + stair[i])
#     print(dp[-1])


# # 계단 오르기
# import sys
# input = sys.stdin.readline
# N = int(input())
# stair = [int(input()) for i in range(N)]

# print(stair)

# def search(n, s):
#     if n
#     a = stair[n]+stair[n+1]+stair[n+3]
#     b = stair[n]+stair[n+2]+stair[n+3]
#     if a >= b:
#         s = a
#         search(n+3, s)
#     else:
#         s = b
#         search(n+3, s)
