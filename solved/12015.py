def find(value):
    left = 0
    right = len(series) - 1

    while left <= right:
        mid = (left + right) // 2
        if series[mid] == value:
            return mid
        else:
            # search left
            if series[mid] > value:
                right = mid - 1
            # search right
            else:
                left = mid + 1

    return left


N = int(input())
numbers = list(map(int, input().split()))

series = [numbers[0]]

for value in numbers:
    if value > series[-1]:
        series.append(value)
    else:
        index = find(value)
        series[index] = value

print(len(series))
