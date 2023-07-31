# N과 M(1)
from itertools import permutations
N, M = map(int, input().split())
nums = [i for i in range(1, N+1)]
for i in permutations(nums, M):
    print(*i)


# import sys
# input = sys.stdin.readline

# def backtracking():
#     if len(array) == m:
#         print(" ".join(map(str, array)))
#         return

#     for i in range(1, n+1):
#         if i not in array:
#             array.append(i)
#             backtracking()
#             array.pop()

# n, m = map(int,input().split())
# array = []

# backtracking()
