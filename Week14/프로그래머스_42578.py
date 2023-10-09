# 의상
from collections import defaultdict


def solution(clothes):
    dic_cloth = defaultdict(int)
    for cloth in clothes:
        dic_cloth[cloth[1]] += 1

    answer = 1
    if dic_cloth:
        for i in dic_cloth.values():
            answer *= i+1
        answer -= 1
    else:
        answer = 0

    return answer
