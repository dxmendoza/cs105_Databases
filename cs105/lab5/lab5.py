from rps import make_bot1_move, make_bot2_move


def check_move(x: str) -> None:
    if x!="r" and x!="p" and x!="s":
        raise Exception("ERROR: invalid move!")

def calculate_winner(x: str, y: str) -> int:
    check_move(x)
    check_move(y)
    if (x == "r" and y == "s") or \
            (x == "p" and y == "r") or \
            (x == "s" and y == "p"):
        return 0
    elif (x == "s" and y == "r") or \
            (x == "r" and y == "p") or \
            (x == "p" and y == "s"):
        return 1
    else:
        return None

def play_rps() -> int:
    x: str = make_bot1_move()
    y: str = make_bot2_move()
    return calculate_winner(x, y)
