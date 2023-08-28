import sys
from collections import defaultdict
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

#  p 포켓몬 진화 위해 k 개 사탕 필요. 진화 후 2개 사탕 돌려 받음(각 포켓몬은 그들 종의 사탕으로만 진화 가능)
#  가장 많이 진화 시킬 수 있는 포켓몬 무엇. 여러 종이면 도감 번호 작은 것 출력, 즉 입력데이터에서 먼저 나타나는것

n = int(input())
result = defaultdict(int)
for _ in range(n):
    name = str(input().strip())
    k, m = map(int, input().split())
    cnt = 0
    while k <= m:
        m = m-k+2
        cnt += 1
    result[name] = cnt

print(sum(result.values()))
result = sorted(result.items(), key=lambda x: x[1], reverse=True)
print(result[0][0])
