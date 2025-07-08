
# assume that there are two variables already created (but you can't see them in this file)
# they look like this:

 # human_move: str = ... # this variable contains one of "r", "p", "s"
 # bot_move: str = ...   # some variable contains one of "r", "p", "s"

did_human_win: bool = None  # put nothing inside this boolean variable (for now)
                            # your job is to decide if the human won! (i.e. contain True if the human won and False otherwise)
# add your code below!
if (human_move == "r" and bot_move == "s") or\
    (human_move == "p" and bot_move == "r") or\
    (human_move == "s" and bot_move == "p"):
    did_human_win = True
else:
    did_human_win = False