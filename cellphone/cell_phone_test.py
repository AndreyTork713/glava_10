import cellphone

def main():
    man = input('Введите марку телефона: ')
    mod = input('Введите модель телефона: ')
    retail = float(input('Введите розничную цену телефона: '))

    cell = cellphone.Cellphone(man, mod, retail)
    print(f'Марка телефона: {cell.get_manufact()}')
    print(f'Модель телефона: {cell.get_model()}')
    print(f'Розничная цена телефона: {cell.get_retail_price()} руб.')


if __name__== '__main__':
    main()