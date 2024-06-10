n = int(input()) + 1

for i in range(1, n):
    inp = input().split()
    globals()['xy_{}'.format(i)] = []
    globals()['xy_{}'.format(i)].append(int(inp[0]))
    globals()['xy_{}'.format(i)].append(int(inp[1]))

for i in range(1, n):
    for j in range(1, n - i):
        if globals()['xy_{}'.format(i)][0] > globals()['xy_{}'.format(i + j)][0]:
            globals()['xy_{}'.format(i)], globals()['xy_{}'.format(i + j)] = globals()['xy_{}'.format(i + j)], globals()['xy_{}'.format(i)]
            break
        else:
            break

for i in range(1, n):
    for j in range(1, n - i):
        if globals()['xy_{}'.format(i)][0] == globals()['xy_{}'.format(i + j)][0]:
            if globals()['xy_{}'.format(i)][1] > globals()['xy_{}'.format(i + j)][1]:
                globals()['xy_{}'.format(i)], globals()['xy_{}'.format(i + j)] = globals()['xy_{}'.format(i + j)], globals()['xy_{}'.format(i)]
                break

for i in range(1, n):
    print(str(globals()['xy_{}'.format(i)][0]) + " " + str(globals()['xy_{}'.format(i)][1]))