def solution(N, number):
    dp = []  # 얻을 수 있는 숫자

    for i in range(1, 9):
        case = set()
        case.add(int(str(N) * i))  # N 반복해서 더한 수
        for j in range(0, i - 1):  # (1, n-1) 부터 (n-1, 1)까지 사칙연산
            for a in dp[j]:
                for b in dp[-1 - j]:
                    case.add(a - b)
                    case.add(a + b)
                    case.add(a * b)
                    if b != 0:
                        case.add(a // b)

        if number in case:  # 목표 숫자있는지 확인
            answer = i
            break
        dp.append(case)  # 다음 단계에서 사용위해 append
    else:
        answer = -1
    return answer
