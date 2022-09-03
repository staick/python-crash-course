# 9-13. Dice
from random import randint

class Dice:

    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

dice_6 = Dice()
for num in range(10):
    dice_6.roll_die()

dice_10 = Dice(10)
for num in range(10):
    dice_10.roll_die()

dice_20 = Dice(20)
for num in range(10):
    dice_20.roll_die()
