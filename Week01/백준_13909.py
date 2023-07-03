import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
x = 1
while x*x <= N:
    x += 1
    cnt += 1
print(cnt)


# import sys
# input = sys.stdin.readline

# N = int(input())
# cnt = 0
# x = 1
# for x in range(1, N+1):
#     if x*x <= N:
#         x += 1
#         cnt += 1
# print(cnt)


# N = int(input())
# window = {}

# for person in range(N):
#     for i in range(0, N, person + 1):
#         if i not in window or window[i] == 0:
#             window[i] = 1
#         else:
#             window[i] = 0

# print(sum(window.values()))
