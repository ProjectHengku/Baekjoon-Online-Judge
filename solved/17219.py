N, M = map(int, input().split())
IDPW = {}

for _ in range(N):
    site, password = input().split()
    IDPW.update({site: password})

for _ in range(M):
    site = input()
    print(IDPW.get(site))
