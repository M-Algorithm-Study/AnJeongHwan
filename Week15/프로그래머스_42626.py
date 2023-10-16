# 더 맵게
import heapq


def solution(scoville, K):

    heapq.heapify(scoville)
    cnt = 0
    while scoville[0] < K:
        if len(scoville) == 0:
            return -1

        cnt += 1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        new = first + second*2
        heapq.heappush(scoville, new)

    return cnt
