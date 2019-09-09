from typing import List

def checkio(game_result: List[str]) -> str:
    x = game_result[0]
    y = game_result[1]
    z = game_result[2]
    if x[0] == x[1] == x[2] != ".":
        return x[0]
    elif y[0] == y[1] == y[2] != ".":
        return y[0]
    elif z[0] == z[1] == z[2] != ".":
        return z[0]
    elif x[0] == y[1] == z[2] != ".":
        return x[0]
    elif z[0] == y[1] == x[2] != ".":
        return z[0]
    for i in range(0, 3):
        if x[i] == y[i] == z[i] != ".":
            return x[i]
    else:
        draw = "D"
        return draw



if __name__ == '__main__':
    print("Example:")
    print(checkio(["O..",
                   "OOX",
                   "OO."]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")