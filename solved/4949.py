import sys

input = sys.stdin.readline

while True:
    sentence = input()
    check = []
    wrong = []

    if sentence == ".\n":
        exit()

    for letter in sentence:
        if letter == "(":
            check.append(letter)
        elif check and check[len(check) - 1] == "(" and letter == ")":
            check.pop()
        elif letter == "[":
            check.append(letter)
        elif check and check[len(check) - 1] == "[" and letter == "]":
            check.pop()
        elif len(check) == 0 and (letter == ")" or letter == "]"):
            wrong.append(letter)
            break
        elif check and (
            (check[len(check) - 1] == "(" and letter == "]")
            or (check[len(check) - 1] == "[" and letter == ")")
        ):
            wrong.append(letter)
            break

    if len(check) == 0 and len(wrong) == 0:
        print("yes")
    else:
        print("no")
