# Assume that this variable exists, but we don't know its exact value! You do know that it will be
# between [0.0, 100.0] inclusive (it could contain 0.0 or 100.0, or anything in between).
percent: float = 0.0


# Be sure to set this variable with the solid letter grade (no +/- letter grades) using the standard
# percents (90.0 or above is an "A", 80.0 is a "B", etc.)
grade: str = None

if percent >= 90:
    grade = "A"
elif percent >= 80:
    grade = "B"
elif percent >= 70:
    grade = "C"
elif percent >= 60:
    grade = "D"
else:
    grade = "F"

