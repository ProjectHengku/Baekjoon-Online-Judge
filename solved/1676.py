N = int(input())

# N! 구하기
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
    
# N!을 문자열로 변환
num = str(factorial(N))

# 뒤에서부터 0의 개수 구하기
count = 0
for i in range(len(num) - 1, -1, -1):
    if num[i] == '0':
        count += 1
    else:
        break

print(count)