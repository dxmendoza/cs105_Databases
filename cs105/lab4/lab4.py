# place your code below!
import math

sqrt20: float = math.sqrt(20)
fact6: int = math.factorial(6)
log150: float = math.log(150)
elog150: float = math.exp(log150)
isClose: int = None
if math.isclose(elog150, 150, rel_tol=1e-06, abs_tol=0.0):
    isClose = 1
else:
    isClose = -1

def is_even(x: int) -> bool:
    if x % 2 == 0:
        return True
    else:
        return False

def get_solid_letter_grade(x: float) -> str:
    if x >= 90:
        return "A"
    elif x >= 80:
        return "B"
    elif x >= 70:
        return "C"
    elif x >= 60:
        return "D"
    else:
        return "F"

def has_passed(x: float) -> bool:
    y: str = get_solid_letter_grade(x)
    if y=="A" or y=="B" or y=="C":
        return True
    else:
        return False

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


