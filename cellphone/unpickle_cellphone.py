import pickle
import cellphone
# Константа для имени файла
FILENAME = 'cellphones.dat'

def main():
    end_of_file = False # Переменная для обозначения конца файла

    # Открыть файл
    input_file = open(FILENAME, 'rb')

    while not end_of_file:
        try:
            # Расконсервировать следующий объект
            phone = pickle.load(input_file)
            # Показать расконсервированные данные
            display_data(phone)
        except EOFError:
            # Установить, что был достигнут конец файла
            end_of_file = True

    # Закрыть файл
    input_file.close()


def display_data(phone):

    print(f'Производитель телефона: {phone.get_manufact()}')
    print(f'Модель телефона: {phone.get_model()}')
    print(f'Розничная цена телефона: {phone.get_retail_price():,.2f}')


if __name__ == '__main__':
    main()