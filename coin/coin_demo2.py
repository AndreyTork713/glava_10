from coin import coin


def main():
    # Создать объект класса Coin
    my_coin = coin.Coin()

    # Показать обращенную вверх сторону монеты
    print('Эта сторона обращена вверх: ', my_coin.get_sideup())

    # Подбросит монету
    print('Подбрасываю монету...')
    my_coin.toss()

    # # К параметрам объекта имеет доступ кто-угодно
    # my_coin.sideup = 'Орел'

    # Показать обращенную вверх сторону монеты
    print('Эта сторона обращена вверх: ', my_coin.get_sideup())


if __name__ == '__main__':
    main()