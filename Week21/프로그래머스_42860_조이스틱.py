def solution(name):
    alpha_cnt = 0
    cursor_cnt = len(name) - 1  # 최소 이동 횟수는 길이 - 1

    for i, alpha in enumerate(name):
        alpha_cnt += min(ord(alpha) - 65, 91 - ord(alpha))  # 위로 or 아래로 최솟값
        # A: 65 Z: 90

        # 해당 알파벳 다음부터 연속된 A
        next = i + 1
        while next < len(name) and name[next] == "A":
            next += 1

        # 기본 최소 길이, 연속된 A의 왼쪽시작, 연속된 A의 오른쪽시작 비교
        cursor_cnt = min(
            [cursor_cnt, 2 * i + len(name) - next, i + 2 * (len(name) - next)]
        )

    answer = cursor_cnt + alpha_cnt
    return answer


# 풀이 참고

# def solution(name):
#     # name을 반대로 AAAA로 만들면 된다.
#     # A: 65 Z: 90
#     # 커서 이동 횟수, 알파벳 변경 횟수
#     cursor_cnt, alpha_cnt = 0, 0
#     max_a_count = 0  # 연속된 A의 수의 최댓값
#     temp_a_count = 0

#     for idx, alpha in enumerate(name):
#         cursor_cnt += 1
#         alpha_cnt += min(ord(alpha) - 65, 91 - ord(alpha))  # 위로 or 아래로 최솟값

#         while idx < len(name) - 1 and name[idx + 1] == "A":  # 최댓값 찾기
#             temp_a_count += 1
#             idx += 1

#         if temp_a_count > max_a_count:
#             max_a_count = temp_a_count
#         temp_a_count = 0

#     if name.count("A") == 1:
#         max_a_count = 1

#     answer = cursor_cnt - 1 + alpha_cnt - max_a_count

#     return answer


# def solution(name):
#     # name을 반대로 AAAA로 만들면 된다.
#     # A: 65 Z: 90
#     cnt = 0
#     for alpha in name:
#         if alpha == "A":
#             cnt += 1
#         else:
#             a = ord(alpha) - 65
#             b = 91 - ord(alpha)
#             cnt += 1
#             cnt += min(a, b)

#     cnt2 = 1
#     for alpha in name[::-1]:
#         if alpha == "A":
#             cnt2 += 1
#         else:
#             a = ord(alpha) - 65
#             b = 91 - ord(alpha)
#             cnt2 += 1
#             cnt2 += min(a, b)

#     print(min(cnt, cnt2))
#     answer = min(cnt, cnt2)

#     return answer
