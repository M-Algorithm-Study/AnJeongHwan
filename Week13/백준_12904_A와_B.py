import sys
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

# S를 T로 만들 수 있는지 없는지
# 문자열의 뒤에 A를 추가한다.
# 문자열을 뒤집고 뒤에 B를 추가한다.

S = input().strip()
T = input().strip()

# T의 길이가 S보다 길 때까지 아래 코드를 반복
while len(T) > len(S):
    # T의 마지막 문자가 'A'일 경우, 해당 문자를 제거
    if T[-1] == 'A':
        T = T[:-1]
    # T의 마지막 문자가 'B'일 경우, 해당 문자를 제거하고 T를 뒤집기
    elif T[-1] == 'B':
        T = T[:-1]
        T = T[::-1]

# S와 T가 같다면 1을 출력하고, 다르다면 0을 출력
if S == T:
    print(1)
else:
    print(0)
