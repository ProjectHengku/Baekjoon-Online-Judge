import sys
import heapq

input = sys.stdin.readline

T = int(input())

for t in range(T):
    k = int(input())

    # max(), min() 속도가 느려서 힙 큐 알고리즘으로 최대-최소값을 각각 따짐
    maxQheap = []
    minQheap = []
    # Q에 실제 값 대신 값 기록 유무를 저장함
    Q = [0] * k

    for i in range(k):
        command = input().split()
        num = int(command[1])
        calc = command[0]

        if calc == "I":
            Q[i] = 1
            heapq.heappush(minQheap, (num, i))
            # 최대힙을 만들 때에는 - 붙여서 최솟값 정렬을 최댓값 정렬로 바꿈
            heapq.heappush(maxQheap, (-num, i))
        else:
            if num == 1:
                # 이미 제거된 수 제거
                while maxQheap and Q[maxQheap[0][1]] == 0:
                    heapq.heappop(maxQheap)
                if maxQheap:
                    # 최댓값 삭제
                    Q[maxQheap[0][1]] = 0
                    heapq.heappop(maxQheap)
            else:
                # 이미 제거된 수 제거
                while minQheap and Q[minQheap[0][1]] == 0:
                    heapq.heappop(minQheap)
                if minQheap:
                    # 최댓값 삭제
                    Q[minQheap[0][1]] = 0
                    heapq.heappop(minQheap)

    if 1 not in Q:
        print("EMPTY")
    else:
        # 이미 제거된 수 제거 (동기화)
        while maxQheap and Q[maxQheap[0][1]] == 0:
            heapq.heappop(maxQheap)
        while minQheap and Q[minQheap[0][1]] == 0:
            heapq.heappop(minQheap)

        print(-maxQheap[0][0], minQheap[0][0])
