sequence = [1, 2, 3, 4, 5]
k = 7


def solution(sequence, k):
    start = 0  # 시작 인덱스 초기화
    end = 0  # 마지막 인덱스 초기화
    current_sum = 0  # 현재 부분 수열의 합 초기화
    result = []  # 결과를 담을 리스트 초기화

    while start < len(sequence):
        if current_sum < k:  # 현재 합이 k보다 작을 경우
            if end == len(sequence):  # 마지막 인덱스에 도달한 경우
                break
            current_sum += sequence[end]  # 현재 합에 다음 원소 추가
            end += 1  # 마지막 인덱스 증가

        elif current_sum >= k:  # 현재 합이 k 이상일 경우
            if current_sum == k:  # 현재 합이 k와 동일한 경우
                if not result or (end - start - 1) < (result[1] - result[0]):
                    # 결과가 없거나 현재 수열이 더 짧을 경우에만 업데이트
                    result = [start, end - 1]  # 결과 업데이트
            current_sum -= sequence[start]  # 현재 합에서 첫 번째 원소 제거
            start += 1  # 시작 인덱스 증가

    return result


# # 시간초과 풀이
# def solution(sequence, k):
#     current_sum = 0
#     start = -1
#     end = -1
#     result = [start, end]
#     min_length = len(sequence)
#     for s in range(len(sequence)):
#         current_sum = 0
#         start = -1
#         end = -1
#         for i in range(s, len(sequence)):
#             if sequence[i] == k:
#                 result = [i, i]
#                 return result

#             current_sum += sequence[i]

#             if start == -1:
#                 start = i
#             elif current_sum > k:
#                 current_sum = 0
#                 start = -1
#                 end = -1
#             elif current_sum == k:
#                 end = i
#                 if min_length > (end - start):
#                     result = [start, end]
#                     min_length = result[1]-result[0]
#                 current_sum = 0
#                 start = -1
#                 end = -1

#     return result


# solution(sequence, k)
