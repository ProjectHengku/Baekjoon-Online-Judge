import copy

N, M = map(int, input().split())
numbers = [list(map(int, input().split())) for _ in range(N)]

# 테트로미노 경우의 수
o = [[1, 1], [1, 1]]
i = [[1, 1, 1, 1]]
l = [[1, 1, 1], [0, 0, 1]]
t = [[1, 1, 1], [0, 1, 0]]
s = [[1, 0], [1, 1], [0, 1]]

# 이걸 돌리고 뒤집을 수 있겠네
# i는 90도 돌리기
i90 = [list(row) for row in zip(*i[::-1])]
# t는 90 180 270 돌리기
t90 = [list(row) for row in zip(*t[::-1])]
t180 = [list(row) for row in zip(*t90[::-1])]
t270 = [list(row) for row in zip(*t180[::-1])]
# l과 s는 90 180 270 돌리고, 좌우 뒤집기에서도 동일
l90 = [list(row) for row in zip(*l[::-1])]
l180 = [list(row) for row in zip(*l90[::-1])]
l270 = [list(row) for row in zip(*l180[::-1])]

lr = [row[::-1] for row in l]
lr90 = [list(row) for row in zip(*lr[::-1])]
lr180 = [list(row) for row in zip(*lr90[::-1])]
lr270 = [list(row) for row in zip(*lr180[::-1])]

s90 = [list(row) for row in zip(*s[::-1])]
s180 = [list(row) for row in zip(*s90[::-1])]
s270 = [list(row) for row in zip(*s180[::-1])]

sr = [row[::-1] for row in s]
sr90 = [list(row) for row in zip(*sr[::-1])]
sr180 = [list(row) for row in zip(*sr90[::-1])]
sr270 = [list(row) for row in zip(*sr180[::-1])]

tets = [
    o,
    i,
    i90,
    t,
    t90,
    t180,
    t270,
    l,
    l90,
    l180,
    l270,
    lr,
    lr90,
    lr180,
    lr270,
    s,
    s90,
    s180,
    s270,
    sr,
    sr90,
    sr180,
    sr270,
]

maxscore = float("-inf")
for tet in tets:
    n = len(tet)
    m = len(tet[0])

    for y in range(N - n + 1):
        for x in range(M - m + 1):
            score = 0
            for i in range(n):
                for j in range(m):
                    if tet[i][j] == 1:
                        score += numbers[y + i][x + j]

            if score > maxscore:
                maxscore = score

print(maxscore)
