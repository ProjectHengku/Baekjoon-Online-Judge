N, M = map(int, input().split())
tree = list(map(int, input().split()))

# 가운데부터 시작
start = max(tree)
end = 0

# 더 많으면 올리고 더 적으면 내린다
while start >= end:
    mid = (start + end) // 2
    # 자를 수 있으면 자른다
    cut = sum([length - mid if mid < length else 0 for length in tree])

    # 더 많으면 상향 조정
    if cut >= M:
        if mid == end:
            mid += 1
        end = mid
    # 너무 적으면 내린다
    else:
        if mid == start:
            mid -= 1
        start = mid


print(mid)
