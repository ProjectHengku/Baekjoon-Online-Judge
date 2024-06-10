def game_simulate(winner):
    global turn_score, game_score
    if turn_score[winner] == 3:
        for player in turn_score:
            if player != winner and turn_score[player] >= 2:
                break
        else:
            game_score[winner] += 1
            turn_score = {chr(i): 0 for i in range(ord("A"), ord("A") + N)}
            return 1

    if turn_score[winner] == 4:
        game_score[winner] += 1
        turn_score = {chr(i): 0 for i in range(ord("A"), ord("A") + N)}
        return 2

    case3 = False
    for player in turn_score:
        if player != winner and turn_score[player] == 4:
            game_score[player] -= 1
            case3 = True
    if case3:
        return 3

    turn_score[winner] += 1
    return 4


def set_simulate(winner):
    global game_score, set_score
    if game_score[winner] >= 6:
        isperfect = True
        max_score = 0
        for player in game_score:
            if player != winner:
                max_score = max(max_score, game_score[player])
                if game_score[player] != 0:
                    isperfect = False

        if game_score[winner] >= max_score + 2:
            if isperfect:
                set_score[winner] += 2
            else:
                set_score[winner] += 1
            game_score = {chr(i): 0 for i in range(ord("A"), ord("A") + N)}

            if set_score[winner] >= 3:
                print(winner)
                exit()
            return 0


N, S = input().split()
N = int(N)

turn_score = {chr(i): 0 for i in range(ord("A"), ord("A") + N)}
game_score = {chr(i): 0 for i in range(ord("A"), ord("A") + N)}
set_score = {chr(i): 0 for i in range(ord("A"), ord("A") + N)}

for winner in S:
    game_simulate(winner)
    set_simulate(winner)
