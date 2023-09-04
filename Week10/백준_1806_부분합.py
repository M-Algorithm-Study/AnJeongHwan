import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# 입력 받기
N, S = map(int, input().split())  # N: 수열의 길이, S: 부분합의 목표값
sequence = list(map(int, input().split()))  # 수열

# 초기화
min_length = N + 1  # 최소 길이를 초기값으로 설정
start, end = 0, 0  # 부분합을 계산할 시작과 끝 인덱스
partial_sum = 0  # 현재 부분합

while True:
    # 현재 부분합이 목표값 S보다 작은 경우
    if partial_sum < S:
        if end == N:  # 더 이상 끝까지 갈 수 없을 때
            break
        partial_sum += sequence[end]  # 다음 요소를 부분합에 추가
        end += 1  # 끝 인덱스 증가
    # 현재 부분합이 목표값 S보다 크거나 같은 경우
    elif partial_sum >= S:
        # 최소 길이 갱신
        if min_length > end - start:
            min_length = end - start
        partial_sum -= sequence[start]  # 시작 요소를 부분합에서 제거
        start += 1  # 시작 인덱스 증가

# 최소 길이 출력
if min_length != N + 1:
    print(min_length)
else:
    print(0)
