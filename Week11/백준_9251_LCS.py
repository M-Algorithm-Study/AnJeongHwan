import sys
read = sys.stdin.readline

word1, word2 = read().strip(), read().strip()
l1, l2 = len(word1), len(word2)
cache = [0] * l2

for i in range(l1):
    cnt = 0
    for j in range(l2):
        if cnt < cache[j]:
            cnt = cache[j]
        elif word1[i] == word2[j]:
            cache[j] = cnt + 1
print(max(cache))


# # 첫 번째 문자열(word1)의 각 문자에 대해 반복합니다.
# for i in range(l1):
#     cnt = 0  # 현재 문자와 비교되는 문자열(word2)에서 가장 긴 공통 부분 수열의 길이를 저장하는 변수
#     # 두 번째 문자열(word2)의 각 문자에 대해 반복합니다.
#     for j in range(l2):
#         if cnt < cache[j]:  # 현재까지의 최대 LCS 길이보다 크다면
#             cnt = cache[j]  # cnt를 업데이트하여 현재까지의 최대 LCS 길이를 저장합니다.
#         elif word1[i] == word2[j]:  # 현재 문자가 공통 부분 수열에 속한다면
#             cache[j] = cnt + 1  # cache[j]를 업데이트하여 새로운 LCS 길이를 저장합니다.

# # 모든 문자에 대한 처리가 끝난 후, cache 리스트에서 가장 큰 값을 찾아 출력합니다.
# print(max(cache))
