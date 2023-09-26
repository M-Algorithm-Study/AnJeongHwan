import sys
input = sys.stdin.readline
N = int(input())  # 이동하려고 하는 채널
M = int(input())  # 고장난 버튼의 개수
buttons = list(map(int, input().split()))  # 고장난 버튼

# 현재 채널에서 + 혹은 -만 사용하여 이동하는 경우
min_count = abs(100 - N)

for nums in range(1000001):  # N (0 ≤ N ≤ 500,000)
    str_nums = str(nums)

    for j in range(len(str_nums)):
        # 각 숫자가 고장났는지 확인 후, 고장 났으면 break
        if int(str_nums[j]) in buttons:
            break

        # 고장난 숫자 없이 마지막 자리까지 왔다면 min_count 비교 후 업데이트
        elif j == len(str_nums) - 1:
            min_count = min(min_count, abs(int(str_nums) - N) + len(str_nums))

print(min_count)

# # 시도한 풀이
# sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline

# N = int(input())  # 이동하려고 하는 채널
# M = int(input())  # 고장난 버튼의 개수
# buttons = list(map(int, input().split()))  # 고장난 버튼
# # print(N, M, buttons)
# str_N = str(N)
# # 0~9
# # +-
# cnt = 0
# if N == 100:
#     cnt = 0
# elif abs(N - 100) < len(str_N):
#     cnt = abs(N-100)
# else:
#     temp = ''
#     cnt2 = 0
#     for i in str_N:
#         i = int(i)
#         i2 = int(i)
#         while True:
#             if i not in buttons:
#                 temp += str(i)
#                 break
#             elif i2 not in buttons:
#                 temp += str(i2)
#                 break
#             else:
#                 i = i-1
#                 i2 = i2 + 1
#                 if i < 0:
#                     i = 10 + i
#                 if i2 > 10:
#                     i2 = i2 - 10
#                 cnt2 += 1
#     print(len(str_N), (N - int(temp)), int(temp))
#     cnt = len(str_N) + abs(N - int(temp))

# print(cnt)
