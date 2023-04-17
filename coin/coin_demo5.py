from coin import coin


def main():

    coin1 = coin.Coin()
    coin2 = coin.Coin()
    coin3 = coin.Coin()

    print('Показать какой стороной лежат монеты')
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    print()
    print('Подбрасываю монеты')
    coin1.toss()
    coin2.toss()
    coin3.toss()
    print()
    print('Показать какой стороной теперь лежат монеты')
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())


if __name__ == '__main__':
    main()