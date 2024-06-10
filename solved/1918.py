infix = input()

# 초기값 세팅
stack = []
postfix = ""
# 삽입 우선순위, 내부 우선순위
operator = "(/*+-)"
icp = {"(": 3, "/": 2, "*": 2, "+": 1, "-": 1}
isp = {"(": 0, "/": 2, "*": 2, "+": 1, "-": 1}

# 변환
for letter in infix:
    # 연산자인 경우
    if letter in operator:
        if not stack:
            stack.append(letter)
        else:
            # 괄호 닫히면
            if letter == ")":
                # 괄호 사이에 있는거 다 꺼냄
                while stack[-1] != "(":
                    temp = stack.pop()
                    postfix += temp
                stack.pop()
            # 나머지
            else:
                # 연산자 우선순위가 만족될 때 까지 꺼냄
                while stack and icp[letter] <= isp[stack[-1]]:
                    temp = stack.pop()
                    postfix += temp
                stack.append(letter)
    # 피연산자인 경우
    else:
        postfix += letter

# 남은거 다 털어냄
while stack:
    temp = stack.pop()
    postfix += temp

print(postfix)
