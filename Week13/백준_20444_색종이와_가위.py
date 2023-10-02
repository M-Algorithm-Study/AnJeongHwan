import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# 이진 탐색을 위한 왼쪽(left)과 오른쪽(right) 경계를 초기화
left, right = 0, n // 2 + 1

# YES/NO flag 변수 초기화
flag = False

# 이진 탐색을 시작. left가 right와 같아질 때까지 반복
while left != right:
    # 중간 지점을 계산
    mid = (left + right) // 2

    # 중간 지점에서 만들어지는 조각의 수를 계산
    data = (mid + 1) * (n - mid + 1)

    # 조각의 수와 목표 조각의 수 k를 비교
    if data == k:
        # 조건이 충족되면 flag를 True로 설정하고 반복을 종료
        flag = True
        break

    elif data > k:
        # 중간 지점에서 만들어지는 조각의 수가 목표보다 크다면,
        # 오른쪽 경계를 중간 지점 앞으로 이동
        right = mid

    else:
        # 중간 지점에서 만들어지는 조각의 수가 목표보다 작다면,
        # 왼쪽 경계를 중간 지점 다음으로 이동
        left = mid + 1

# flag가 True이면 'YES'를 출력
if flag:
    print("YES")
else:
    # flag가 False이면  'NO'를 출력
    print("NO")


# import sys
# sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline
# n, k = map(int, input().split())

# left, right = 0, n // 2 + 1
# flag = False
# while left != right:
#     mid = (left + right) // 2
#     data = (mid + 1) * (n - mid + 1)

#     if data == k:
#         flag = True
#         break

#     elif data > k:
#         right = mid

#     else:
#         left = mid + 1

# if flag:
#     print("YES")
# else:
#     print("NO")
