# Программа создает 5 объектов Cellphone и сохраняет их в списке
import cellphone


def main():

    # Получить список объектов Cellphone
    phones = make_list()

    # Показать данные в списке
    print('Вот введенные вами данные: ')
    display_list(phones)


def make_list():
    phone_list = []

    for count in range(1, 6):
        # Получить данные
        print(f'Номер телефона: {count}')
        man = input('Введите производителя телефона: ')
        mod = input('Введите модель телефона: ')
        retail = int(input('Введите розничную цену телефона: '))
        print()

        # Создать объект с полученными данными
        phone = cellphone.Cellphone(man, mod, retail)
        # Внести объект в список
        phone_list.append(phone)
    return phone_list


def display_list(phone_list):
    for item in phone_list:
        print(item.get_manufact())
        print(item.get_model())
        print(item.get_retail_price())
        print()


if __name__ == '__main__':
    main()