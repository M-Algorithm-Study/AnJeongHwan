n = int(input())
lists = []
dp = [1]*n

for i in range(n):
    a, b = map(int, input().split())
    lists.append([a, b])

lists.sort()

for i in range(1, n):
    for j in range(0, i):
        if lists[j][1] < lists[i][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))

# import sys
# sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline

# n = int(input())
# dp = [1]*(n+1)
# nums = []
# for i in range(n):
#     a, b = map(int, input().split())
#     nums.append((a, b))
# print(nums)
# nums = sorted(nums, key=lambda x: x[0])
# print(nums)

# max_result = 0
# # for i in range(n):
# #     if nums[i] > nums[i-1]
