
# Assume that these two variables exist, but you don't know their exact contents!
# For example, c1 could contain "Jack" and c2 could contain "2" but we don't know!
# c1: str = ...
# c2: str = ...

# make sure to populate this variable with True if you want another card (i.e. the total # of points in your hand
# is < 17, and False otherwise)
hit: bool = None

if c1 == "Ace":
    c1 = 11
elif c1 == "King" or c1 == "Queen" or c1 == "Jack":
    c1 = 10
else:
    c1 = int(c1)

if c2 == "Ace":
    c2 = 11
elif c2 == "King" or c2 == "Queen" or c2 == "Jack":
    c2 = 10
else:
    c2 = int(c2)

if c1 + c2 < 17:
    hit = True
else:
    hit = False