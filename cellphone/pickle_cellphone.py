# Программа консервации объектов Cellphone.
import pickle
import cellphone

# Константа для имени файла
FILENAME = 'cellphones.dat'


def main():
    # Переменная для управления циклом
    again = 'y'

    # Открыть файл для записи
    output_file = open(FILENAME, 'wb')

    # Получить данные от пользователя
    while again.lower() == 'y':
        print('Заполните данные телефона.')
        man = input('Введите марку телефона: ')
        mod = input('Введите модель телефона: ')
        retail = int(input('Введите розничную цену телефона: '))

        # Создать объект с заданными атрибутами
        phone = cellphone.Cellphone(man, mod, retail)
        # Законсервировать объект
        pickle.dump(phone, output_file)
        again = input('Продолжать консервацию объектов? y/n ')

    # Закрыть файл
    output_file.close()
    print('Объекты законсервированы в файл cellphones.dat')


if __name__ == '__main__':
    main()