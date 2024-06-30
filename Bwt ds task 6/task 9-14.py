from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

# Create a 6-sided die and roll it 10 times
die_6 = Die()
results_6 = [die_6.roll_die() for _ in range(10)]
print("10 rolls of a 6-sided die:", results_6)

# Create a 10-sided die and roll it 10 times
die_10 = Die(10)
results_10 = [die_10.roll_die() for _ in range(10)]
print("10 rolls of a 10-sided die:", results_10)

# Create a 20-sided die and roll it 10 times
die_20 = Die(20)
results_20 = [die_20.roll_die() for _ in range(10)]
print("10 rolls of a 20-sided die:", results_20)
