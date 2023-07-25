# 영단어 암기는 괴로워
import sys
from collections import defaultdict
input = sys.stdin.readline
N, M = map(int, input().split())
words = defaultdict(int)
for _ in range(N):
    word = input().rstrip()
    if len(word) >= M:  # 단어 길이가 M 이상
        words[word] += 1  # {단어:빈도}

words = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
# -x[1] 빈도수 /  -len(x[0]) 단어 길이 길이의 내림차순 / x[0] 사전 순
for i in words:
    print(i[0])
