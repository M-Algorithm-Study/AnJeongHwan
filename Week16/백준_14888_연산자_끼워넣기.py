import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())  # 사칙연산 기호 개수 입력
answer = []

# res = 현재까지 계산된 결과값, i = 숫자 리스트 A에서 사용할 숫자의 개수


def func(add, sub, mul, div, res=0, i=0):

    # 모든 기호가 0이 된 순간 = 모든 기호를 다 사용한 경우, 현재까지 계산된 결과값을 answer에 append하고 함수를 종료한다.
    if add == 0 and sub == 0 and mul == 0 and div == 0:
        answer.append(res)
        return

    if add > 0:  # 덧셈
        func(add - 1, sub, mul, div, res + A[i], i + 1)
    if sub > 0:  # 뺄셈
        func(add, sub - 1, mul, div, res - A[i], i + 1)
    if mul > 0:  # 곱셈
        func(add, sub, mul - 1, div, res * A[i], i + 1)
    if div > 0:  # 나눗셈
        if res > 0:
            func(add, sub, mul, div - 1, int(res / A[i]), i + 1)
        else:
            func(add, sub, mul, div - 1, -int(-res / A[i]), i + 1)


func(add, sub, mul, div, A[0], 1)
print(max(answer))
print(min(answer))
