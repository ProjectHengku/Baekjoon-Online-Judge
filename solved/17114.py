from collections import deque


M, N, O, P, Q, R, S, T, U, V, W = map(int, input().split())

box = [
    [
        [
            [
                [
                    [
                        [
                            [
                                [
                                    [list(map(int, input().split())) for D2 in range(N)]
                                    for D3 in range(O)
                                ]
                                for D4 in range(P)
                            ]
                            for D5 in range(Q)
                        ]
                        for D6 in range(R)
                    ]
                    for D7 in range(S)
                ]
                for D8 in range(T)
            ]
            for D9 in range(U)
        ]
        for D10 in range(V)
    ]
    for D11 in range(W)
]

# 각 차원축별로 +1, -1씩 이동하므로
d1 = [-1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
d2 = [0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
d3 = [0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
d4 = [0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
d5 = [0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
d6 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
d7 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
d8 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0]
d9 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0]
d10 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0]
d11 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1]

# 현위치 기록장
queue = deque()

# 시작 지점 데이터에 처음 1인 지점의 좌표와 경과일 카운터를 포함
for w in range(W):
    for v in range(V):
        for u in range(U):
            for t in range(T):
                for s in range(S):
                    for r in range(R):
                        for q in range(Q):
                            for p in range(P):
                                for o in range(O):
                                    for n in range(N):
                                        for m in range(M):
                                            if (
                                                box[w][v][u][t][s][r][q][p][o][n][m]
                                                == 1
                                            ):
                                                queue.append(
                                                    [w, v, u, t, s, r, q, p, o, n, m, 0]
                                                )

# 이동 시뮬레이션
while queue:
    now = queue.popleft()
    w, v, u, t, s, r, q, p, o, n, m, count = (
        now[0],
        now[1],
        now[2],
        now[3],
        now[4],
        now[5],
        now[6],
        now[7],
        now[8],
        now[9],
        now[10],
        now[11],
    )
    for i in range(22):
        # 좌표 유효성 체크 후 이동 가능성 체크
        if (
            (0 <= w + d1[i] < W)
            and (0 <= v + d2[i] < V)
            and (0 <= u + d3[i] < U)
            and (0 <= t + d4[i] < T)
            and (0 <= s + d5[i] < S)
            and (0 <= r + d6[i] < R)
            and (0 <= q + d7[i] < Q)
            and (0 <= p + d8[i] < P)
            and (0 <= o + d9[i] < O)
            and (0 <= n + d10[i] < N)
            and (0 <= m + d11[i] < M)
        ) and (
            box[w + d1[i]][v + d2[i]][u + d3[i]][t + d4[i]][s + d5[i]][r + d6[i]][
                q + d7[i]
            ][p + d8[i]][o + d9[i]][n + d10[i]][m + d11[i]]
            == 0
        ):
            # 익었다고 체크하고 한칸씩 이동한다
            box[w + d1[i]][v + d2[i]][u + d3[i]][t + d4[i]][s + d5[i]][r + d6[i]][
                q + d7[i]
            ][p + d8[i]][o + d9[i]][n + d10[i]][m + d11[i]] = 1
            current = [
                w + d1[i],
                v + d2[i],
                u + d3[i],
                t + d4[i],
                s + d5[i],
                r + d6[i],
                q + d7[i],
                p + d8[i],
                o + d9[i],
                n + d10[i],
                m + d11[i],
                count + 1,
            ]
            queue.append(current)

# 익지 못하는 토미토가 남아있는지 확인
for D10 in box:
    for D9 in D10:
        for D8 in D9:
            for D7 in D8:
                for D6 in D7:
                    for D5 in D6:
                        for D4 in D5:
                            for D3 in D4:
                                for D2 in D3:
                                    for D1 in D2:
                                        if 0 in D1:
                                            print(-1)
                                            exit()
else:
    print(count)
