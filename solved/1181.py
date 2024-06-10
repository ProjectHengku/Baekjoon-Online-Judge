n = int(input())
words = []

i = 0

while i < n:
    words.append(input())
    i += 1

# 정렬
i = 0
#j = 0

# 길이가 같으면 사전 순으로
words.sort()
wordd = sorted(set(words))
wordd.sort(key= len)
#print(wordd)

#while i < n:
#    j = 0
#    while j < n - i - 1:
#        if len(words[j]) > len(words[j + 1]):
#            words[j], words[j + 1] = words [j + 1], words[j]
#        j += 1
#    i += 1

    #print(words)



#for i in range(n - 1):
 #   if len(words[i]) == len(words[i + 1]):




#scan = 0

# 중복된 문자 스캔
#while i < n - 1:
#    if len(words[i]) == len(words[i + 1]):
#        if words[i] == words[i + 1]:
#            scan += 1
#    i += 1

#i = 0
#scanf = scan
# 중복된 문자 삭제
#while i < n - 1:
#    if scan == 0:
 #       break
#    if len(words[i]) == len(words[i + 1]):
#        if words[i] == words[i + 1]:
#            words.remove(words[i])
            #print(words)
#            scan -= 1
#    i += 1

#i = 0

for i in range(len(wordd)):
    print(wordd[i])