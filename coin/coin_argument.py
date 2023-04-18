import coin


def main():
    my_coin = coin.Coin()
    print(my_coin.get_sideup())

    flip(my_coin)
    print(my_coin.get_sideup())


def flip(coin_object):
    coin_object.toss()


if __name__ == '__main__':
    main()