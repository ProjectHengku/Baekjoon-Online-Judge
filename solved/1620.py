N, M = map(int, input().split())

# 도감 만들기
collectbyName = {}
collectbyNo = {}
for n in range(N):
    name = input()
    collectbyNo.update({n+1: name})
    collectbyName.update({name: n+1})

for m in range(M):
    question = input()
    if question.isalpha():
        print(collectbyName.get(question))
    else:
        question = int(question)
        print(collectbyNo.get(question))