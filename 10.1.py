import random

# класс Coin имитирует монету
# которую надо подбрасывать

class Coin:
    def __init__(self):
        self.sideup = 'Орел'

    def toss(self):                     # Подбрасывать
        if random.randint(0, 1) == 0:
            self.sideup = 'Орел'
        else:
            self.sideup = 'Решка'


    def get_sideup(self):
        return self.sideup
