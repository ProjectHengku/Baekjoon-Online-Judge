import sys

# input = sys.stdin.readline
output = sys.stdout.write

T = int(input())

for tc in range(T):
    print(f"PROGRAM #{tc+1}:")

    error = False
    code = ""

    # code writer
    while True:
        temp = input()

        if temp == "end":
            break

        for letter in temp:
            if letter == "%":
                break
            else:
                code += letter

    # loop checker
    basket = []
    stack = []
    for cursor, letter in enumerate(code):
        if letter == "[":
            stack.append(cursor)
        elif letter == "]":
            if stack:
                open = stack.pop()
                close = cursor
                basket.append((open, close))
            else:
                error = True
                break
    else:
        if stack:
            error = True

    if error:
        print("COMPILE ERROR")
        continue

    # basket index finder
    find = {}
    for index, value in enumerate(basket):
        open, close = value
        find[open] = index
        find[close] = index

    # brainfuck compiler
    memory = [0] * 32768
    pointer = 0
    cursor = 0
    while cursor < len(code):
        letter = code[cursor]
        if letter == ">":
            pointer = pointer + 1 if pointer + 1 <= 32767 else 0
        elif letter == "<":
            pointer = pointer - 1 if pointer - 1 >= 0 else 32767
        elif letter == "+":
            memory[pointer] = memory[pointer] + 1 if memory[pointer] + 1 <= 255 else 0
        elif letter == "-":
            memory[pointer] = memory[pointer] - 1 if memory[pointer] - 1 >= 0 else 255
        elif letter == ".":
            output(chr(memory[pointer]))
        elif letter == "[":
            if memory[pointer]:
                pass
            else:
                cursor = basket[find[cursor]][1]
                continue
        elif letter == "]":
            if memory[pointer]:
                cursor = basket[find[cursor]][0]
                continue
            else:
                pass

        cursor += 1

    print()
