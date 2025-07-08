# SYSTEM IMPORTS
from typing import List
import random


# PYTHON PROJECT IMPORTS


MOVES: List[str] = ["r", "p", "s"]
BOT1_WEIGHTS = [0.2, 0.3, 0.5]
BOT2_WEIGHTS = [0.5, 0.35, 0.15]


def make_move(weights: List[float]) -> str:
    return random.choices(MOVES, weights=weights)[0]


def make_bot1_move() -> str:
    return make_move(BOT1_WEIGHTS)


def make_bot2_move() -> str:
    return make_move(BOT2_WEIGHTS)


if __name__ == "__main__":
    # code that we don't want to run when this file is imported
    print(make_bot1_move())
    print(make_bot2_move())
