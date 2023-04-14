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


def main():
    # Создать объект класса Coin
    my_coin = Coin()

    # Показать обращенную вверх сторону монеты
    print('Эта сторона обращена вверх: ', my_coin.get_sideup())

    # Подбросит монету
    print('Подбрасывая монету...')
    my_coin.toss()

    # Показать обращенную вверх сторону монеты
    print('Эта сторона обращена вверх: ', my_coin.get_sideup())


if __name__ == '__main__':
    main()