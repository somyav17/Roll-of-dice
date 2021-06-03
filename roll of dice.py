import random
class Dice :
    def roll(self):

        number = random.randint(1,6)
        numver2 = random.randint(1,6)
        return number,numver2



dice = Dice()
print(dice.roll())

