from copy import deepcopy


def turn(string):
    converted = ""
    for digit in string:
        if digit == "6":
            converted = "9" + converted
        elif digit == "9":
            converted = "6" + converted
        else:
            converted = digit + converted
    return converted


def left_is_smaller(l, r):
    a = int(turn(left[l] + right[r]))
    b = int(turn(right[r] + left[l]))
    if a > b:
        return True
    elif a < b:
        return False
    else:
        if len(left[l]) < len(right[r]):
            return True
        else:
            return False


N = int(input())
numbers = list(input().split())

# biggest 'turned' number to add one more chance
biggest = "0"
for number in numbers:
    if len(number) > len(biggest):
        biggest = number
    elif len(number) == len(biggest):
        if int(turn(number)) > int(turn(biggest)):
            biggest = number

numbers.append(biggest)


# merge sort
queue = numbers[:]
next_queue = []

while len(queue) > 1:
    n = len(queue)
    # take two element
    for i in range(0, n, 2):
        if i + 1 < n:
            left, right = queue[i], queue[i + 1]
            temp = []

            if type(left) == str:
                left = [left]
            if type(right) == str:
                right = [right]

            l, r = 0, 0
            l_end, r_end = len(left), len(right)
            while l < l_end or r < r_end:
                if l == l_end:
                    temp.append(right[r])
                    r += 1

                elif r == r_end:
                    temp.append(left[l])
                    l += 1
                else:
                    if left_is_smaller(l, r):
                        temp.append(left[l])
                        l += 1
                    else:
                        temp.append(right[r])
                        r += 1
        # case of single edge element
        else:
            temp = deepcopy(queue[i])
        next_queue.append(temp)
    queue = deepcopy(next_queue)
    next_queue.clear()

ans = "".join(queue[0])
print(ans)
